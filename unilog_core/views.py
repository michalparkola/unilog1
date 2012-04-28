from django.template import Context, loader
from unilog_core.models import Tag, LogEntry
from django.http import HttpResponse

def index(request):
    entries = LogEntry.objects.all().order_by('date')
    return render_to_response('unilog_core/index.html', {'entries': entries})

def detail(request, entry_id):
    return HttpResponse("Hellow Detail View of entry: %s!" % str(entry_id))