from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'unilog_core.views',
    url(r'^$','index'),
    url(r'^(?P<entry_id>\d+)/$', 'detail'),
)