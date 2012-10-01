# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LogEntry.text'
        db.alter_column('unilog_core_logentry', 'text', self.gf('django.db.models.fields.TextField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'LogEntry.text'
        db.alter_column('unilog_core_logentry', 'text', self.gf('django.db.models.fields.CharField')(max_length=500))

    models = {
        'unilog_core.logentry': {
            'Meta': {'ordering': "['-date']", 'object_name': 'LogEntry'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['unilog_core.Tag']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        'unilog_core.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['unilog_core']