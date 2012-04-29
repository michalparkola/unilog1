from django.conf.urls import patterns, include, url

# urlpatterns = patterns(
#    'unilog_core.views',
#    url(r'^$','index'),
#    url(r'^(?P<entry_id>\d+)/$', 'detail'),
#)

from django.views.generic import ListView, DetailView
from unilog_core.models import LogEntry
from unilog_core.views import LogEntriesListView, TaggedEntriesListView

urlpatterns = patterns(
    '',
    url(r'^$',
        LogEntriesListView.as_view(
            queryset = LogEntry.objects.order_by('-date'),
            template_name='unilog_core/index.html'
        )
    ),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=LogEntry,
            context_object_name='entry',
            template_name='unilog_core/details.html'
        )
    ),
    url(r'^(\w+)/$',
        TaggedEntriesListView.as_view(
            template_name='unilog_core/index.html'
        )
    ),
)