# Generated by Django 2.0 on 2018-02-15 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0006_auto_20180215_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='query_notes',
            new_name='notes',
        ),
    ]
