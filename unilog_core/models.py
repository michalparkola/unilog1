from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class LogEntry(models.Model):
    date = models.DateTimeField('Date and time of log entry')
    tags = models.ManyToManyField(Tag)
    text = models.TextField()
    def __unicode__(self):
        return self.text
    
    class Meta:
        ordering = ["-date"]