from datetime import datetime
from fabric.api import env, run, local, cd
from fabric.operations import get

env.hosts = ['ssh.alwaysdata.com']
env.user = "unilog"
env.password = "br23dx"

now = datetime.today().strftime("%Y-%m-%d_%H.%M")
today = datetime.today().strftime("%Y-%m-%d")

backup_dir = ''

def backup_db():
    get('/home/unilog/unilog/db/unilog.db')
    backup_filename = backup_dir + now + "_unilog.db"
    local('mv ssh.alwaysdata.com/unilog.db ' + backup_filename)
    
def backup_all():
    tar_name = now + "_unilog.tgz"
    with cd('/home/unilog/'):
        run ("tar czf " + tar_name + " unilog")
        get('/home/unilog/' + tar_name)
        run ("rm " + tar_name)
    
def clone_repo():
    with cd('/home/unilog/'):
        repo_url = 'https://vertigo@bitbucket.org/vertigo/uni-log'
        run ("hg clone " + repo_url + " " + now + "_unilog.hg")