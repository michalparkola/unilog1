# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LogEntry.user'
        db.add_column('unilog_core_logentry', 'user',
                      self.gf('django.db.models.fields.CharField')(default='vertigo', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LogEntry.user'
        db.delete_column('unilog_core_logentry', 'user')


    models = {
        'unilog_core.logentry': {
            'Meta': {'ordering': "['-date']", 'object_name': 'LogEntry'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['unilog_core.Tag']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'unilog_core.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['unilog_core']