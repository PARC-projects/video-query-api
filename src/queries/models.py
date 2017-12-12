from django.db import models
from django.contrib.postgres.fields import ArrayField


class Dataset(models.Model):
    name = models.CharField(max_length=254, unique=True)

    class Meta:
        db_table = 'video_dataset'


class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT)

    class Meta:
        db_table = 'video'


class Query(models.Model):
    name = models.CharField(max_length=254, unique=True)
    video_dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reference_time = models.TimeField(default='00:00:00')
    max_matches = models.PositiveIntegerField(default=20)
    query_notes = models.TextField()
    reference_clip_image = models.ImageField(default='Picture1.jpg')

    class Meta:
        db_table = 'query'


class MatchArray(models.Model):
    query_name = models.ForeignKey(Query, on_delete=models.PROTECT)
    round = models.PositiveIntegerField()
    matches = ArrayField(models.PositiveIntegerField(), default=[1, 2])  # array of snippet ids
    nearmatches = ArrayField(models.PositiveIntegerField(), default=[3, 4])  # array of snippet ids
    revised_matches = ArrayField(models.PositiveIntegerField(), default=[1, 2])  # array of snippet ids
    match_criterion = models.FloatField()
    near_match_criterion = models.FloatField()
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'match_array'


class Signature(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    snippet = models.PositiveIntegerField()
    signature = ArrayField(models.FloatField())

    class Meta:
        db_table = 'signature'
