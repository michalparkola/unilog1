from django.conf.urls import patterns, include, url

# urlpatterns = patterns(
#    'unilog_core.views',
#    url(r'^$','index'),
#    url(r'^(?P<entry_id>\d+)/$', 'detail'),
#)

from django.views.generic import ListView, DetailView
from unilog_core.models import LogEntry

urlpatterns = patterns(
    '',
    url(r'^$',
        ListView.as_view(
            queryset = LogEntry.objects.order_by('-date'),
            context_object_name='entries',
            template_name='unilog_core/index.html'
        )
    ),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=LogEntry,
            context_object_name='entry',
            template_name='unilog_core/details.html'
        )
    )
)