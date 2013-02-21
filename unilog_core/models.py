from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class LogEntry(models.Model):
    date = models.DateTimeField('Date and time of log entry')
    tags = models.ManyToManyField(Tag, blank = True)
    text = models.TextField()
    user = models.ForeignKey(User, related_name='author')

    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ["-date"]