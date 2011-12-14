# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OnlineCounter'
        db.create_table('online_counter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, db_column='visitor_ip')),
            ('is_user', self.gf('django.db.models.fields.BooleanField')(default=False, db_column='is_user')),
            ('visited_time', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, db_column='visitor_time', blank=True)),
        ))
        db.send_create_signal('onlinecounter', ['OnlineCounter'])


    def backwards(self, orm):
        
        # Deleting model 'OnlineCounter'
        db.delete_table('online_counter')


    models = {
        'onlinecounter.onlinecounter': {
            'Meta': {'object_name': 'OnlineCounter', 'db_table': "'online_counter'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'db_column': "'visitor_ip'"}),
            'is_user': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'is_user'"}),
            'visited_time': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'db_column': "'visitor_time'", 'blank': 'True'})
        }
    }

    complete_apps = ['onlinecounter']
