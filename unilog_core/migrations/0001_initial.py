# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table('unilog_core_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('unilog_core', ['Tag'])

        # Adding model 'LogEntry'
        db.create_table('unilog_core_logentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('unilog_core', ['LogEntry'])

        # Adding M2M table for field tags on 'LogEntry'
        db.create_table('unilog_core_logentry_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('logentry', models.ForeignKey(orm['unilog_core.logentry'], null=False)),
            ('tag', models.ForeignKey(orm['unilog_core.tag'], null=False))
        ))
        db.create_unique('unilog_core_logentry_tags', ['logentry_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table('unilog_core_tag')

        # Deleting model 'LogEntry'
        db.delete_table('unilog_core_logentry')

        # Removing M2M table for field tags on 'LogEntry'
        db.delete_table('unilog_core_logentry_tags')


    models = {
        'unilog_core.logentry': {
            'Meta': {'ordering': "['-date']", 'object_name': 'LogEntry'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['unilog_core.Tag']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'unilog_core.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['unilog_core']