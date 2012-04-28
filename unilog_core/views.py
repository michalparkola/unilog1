from django.shortcuts import render_to_response
from unilog_core.models import Tag, LogEntry
from django.http import Http404

def index(request):
    entries = LogEntry.objects.all().order_by('date')
    return render_to_response('unilog_core/index.html', {'entries': entries})

def detail(request, entry_id):
    try:
        entry = LogEntry.objects.get(pk=entry_id)
    except LogEntry.DoesNotExist:
        raise Http404
    return render_to_response("unilog_core/details.html", {'entry':entry})