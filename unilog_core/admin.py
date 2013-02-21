from unilog_core.models import Tag, LogEntry
from django.contrib import admin

class LogEntryAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('date','user','text')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

    def queryset(self, request):
        if request.user.is_superuser:
                return LogEntry.objects.all()
        return LogEntry.objects.filter(user=request.user)
        
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(LogEntryAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.user.id:
            return False
        return True

admin.site.register(Tag)
admin.site.register(LogEntry, LogEntryAdmin)