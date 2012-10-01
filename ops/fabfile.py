from datetime import datetime
from fabric.api import env, run, local, cd
from fabric.operations import get, put

import urllib2

env.hosts = ['ssh.alwaysdata.com']
env.user = "unilog"
env.password = "br23dx"

now = datetime.today().strftime("%Y-%m-%d_%H-%M")
today = datetime.today().strftime("%Y-%m-%d")

def backup_db():
    get('/home/unilog/unilog/db/unilog.db')
    backup_filename = now + "_unilog.db"
    local('mv ssh.alwaysdata.com/unilog.db ' + backup_filename)
    local('rmdir ssh.alwaysdata.com')

def overwrite_remote_db():
    put('/Users/vertigo/Developer/Unilog/db/unilog.db', '/home/unilog/unilog/db/unilog.db')

def backup():
    tar_name = now + "_unilog.tgz"
    with cd('/home/unilog/'):
        run("tar czf " + tar_name + " unilog")
        get('/home/unilog/' + tar_name)
        run("rm " + tar_name)
    local('mv ssh.alwaysdata.com/* .')
    local('rmdir ssh.alwaysdata.com')
    
def pull_from_bitbucket():
    repo_url = 'https://vertigo@bitbucket.org/vertigo/uni-log'
    with cd('/home/unilog/'):
        run("hg clone " + repo_url)
        run("cp -r uni-log/* unilog")
        run("rm -rf uni-log")

def collectstatic():  
    with cd('/home/unilog/unilog'):
        run("python manage.py collectstatic")

def change_app_root():
    before = "/Users/vertigo/Developer/Unilog/"
    after = "/home/unilog/unilog/"
    with cd('/home/unilog/unilog/unilog/'):
        run("cp settings.py old-settings.py")
        run("sed 's:" + before + ":" + after + ":' <old-settings.py >settings.py")  
        run("rm old-settings.py")

def disable_south():
    with cd('/home/unilog/unilog/unilog/'):
        run("cp settings.py old-settings.py")
        run("""sed "s:'south',:# 'south',:" <old-settings.py >settings.py""")  
        run("rm old-settings.py")

def restart_fcgi():
    urllib2.urlopen("https://admin.alwaysdata.com/advanced/processes/restart/")

def deploy():
    backup_db()
    backup()
    pull_from_bitbucket()
    change_app_root()
    disable_south()
    collectstatic()
    # TODO: syncdb
    # TODO: migratedb
    restart_fcgi()