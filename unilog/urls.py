from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^unilog/$','unilog_core.views.index'),
    url(r'^unilog/(?P<entry_id>\d+)/$', 'unilog_core.views.detail'),

    # Examples:
    # url(r'^$', 'unilog.views.home', name='home'),
    # url(r'^unilog/', include('unilog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
