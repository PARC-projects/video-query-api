# Generated by Django 2.0 on 2017-12-18 21:15

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'dataset',
            },
        ),
        migrations.CreateModel(
            name='MatchedArray',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.PositiveIntegerField()),
                ('matches', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[1, 2], size=None)),
                ('near_matches', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[3, 4], size=None)),
                ('revised_matches', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[1, 2], size=None)),
                ('match_criterion', models.FloatField()),
                ('near_match_criterion', models.FloatField()),
                ('weights', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
            options={
                'db_table': 'matched_array',
            },
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('reference_time', models.TimeField(default='00:00:00')),
                ('max_matches', models.PositiveIntegerField(default=20)),
                ('query_notes', models.TextField()),
                ('reference_clip_image', models.ImageField(upload_to='')),
                ('dataset_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Dataset')),
            ],
            options={
                'db_table': 'query',
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snippet', models.PositiveIntegerField()),
                ('signature', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
            ],
            options={
                'db_table': 'signature',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Dataset')),
            ],
            options={
                'db_table': 'video',
            },
        ),
        migrations.AddField(
            model_name='signature',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Video'),
        ),
        migrations.AddField(
            model_name='query',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queries.Video'),
        ),
        migrations.AddField(
            model_name='matchedarray',
            name='query_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='queries.Query'),
        ),
    ]
