# Generated by Django 2.0.2 on 2018-02-28 19:21

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DnnStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=80, unique=True)),
                ('max_number_of_splits', models.PositiveSmallIntegerField(blank=True, help_text='maximum allowed number of splits for this stream', null=True)),
            ],
            options={
                'db_table': 'dnn_streams',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dnn_stream_split', models.PositiveSmallIntegerField(help_text='Split number of dnn_stream, ensemble averaging is over splits of a given dnn stream.')),
                ('name', models.CharField(help_text='Should match the feature name in the DNN (e.g., Caffe) model.', max_length=80)),
                ('dnn_weights_uri', models.CharField(help_text='Location of the weights file for the CNN model used to compute the feature.', max_length=4096)),
                ('dnn_spec_uri', models.CharField(help_text='Location of the spec for the DNN model, i.e. a prototxt file for Caffe models.', max_length=4096, null=True)),
                ('features', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), help_text='feature vector', size=None)),
                ('dnn_stream', models.ForeignKey(help_text='DNN stream name from dnn_streams table signifying which of the streams in the multi-stream DNN this row belongs.', on_delete=django.db.models.deletion.PROTECT, to='queries.DnnStream', to_field='type')),
            ],
            options={
                'db_table': 'feature',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('is_match', models.BooleanField(default=0)),
                ('reference_time', models.PositiveIntegerField(default=0)),
                ('user_match', models.NullBooleanField(default=None)),
            ],
            options={
                'db_table': 'match',
                'ordering': ('-score',),
            },
        ),
        migrations.CreateModel(
            name='ProcessState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'process_state',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('reference_time', models.TimeField(default='00:00:00')),
                ('max_matches_for_review', models.PositiveIntegerField(default=20)),
                ('notes', models.TextField(null=True)),
                ('reference_clip_image', models.ImageField(null=True, upload_to='')),
                ('current_round', models.PositiveIntegerField(default=1)),
                ('current_match_criterion', models.FloatField(default=0.8)),
                ('current_weights', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('process_state', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='queries.ProcessState')),
            ],
            options={
                'db_table': 'query',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='QueryResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.PositiveIntegerField(default=1)),
                ('match_criterion', models.FloatField(default=0.8)),
                ('weights', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Query')),
            ],
            options={
                'db_table': 'query_result',
            },
        ),
        migrations.CreateModel(
            name='SearchSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'search_set',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('path', models.CharField(max_length=4096)),
                ('search_sets', models.ManyToManyField(to='queries.SearchSet')),
            ],
            options={
                'db_table': 'video',
            },
        ),
        migrations.CreateModel(
            name='VideoClip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clip', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField(default=10)),
                ('debug_video_uri', models.CharField(blank=True, max_length=4096, null=True)),
                ('notes', models.TextField(blank=True, max_length=25600, null=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Video')),
            ],
            options={
                'db_table': 'video_clip',
            },
        ),
        migrations.AddField(
            model_name='query',
            name='search_set_to_query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.SearchSet'),
        ),
        migrations.AddField(
            model_name='query',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Video'),
        ),
        migrations.AddField(
            model_name='match',
            name='query_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.QueryResult'),
        ),
        migrations.AddField(
            model_name='match',
            name='reference_video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reference_video', to='queries.Video'),
        ),
        migrations.AddField(
            model_name='feature',
            name='video_clip',
            field=models.ForeignKey(help_text='Id in the video_clips table for the clip corresponding to this row.', on_delete=django.db.models.deletion.PROTECT, to='queries.VideoClip'),
        ),
        migrations.AlterUniqueTogether(
            name='videoclip',
            unique_together={('video', 'clip', 'duration')},
        ),
        migrations.AlterUniqueTogether(
            name='feature',
            unique_together={('video_clip', 'dnn_stream', 'dnn_stream_split', 'name')},
        ),
    ]
