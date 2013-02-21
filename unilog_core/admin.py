from unilog_core.models import Tag, LogEntry
from django.contrib import admin

class LogEntryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('date','user','text')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Tag)
admin.site.register(LogEntry, LogEntryAdmin)