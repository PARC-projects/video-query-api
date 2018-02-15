from django.db import models
from django.contrib.postgres.fields import ArrayField

from queries.models import VideoClip


class Feature(models.Model):
    video_clip = models.ForeignKey(VideoClip, on_delete=models.PROTECT)
    dnn_stream = models.TextField()
    dnn_stream_split = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=80)
    weights_uri = models.CharField(max_length=4096)
    dnn_spec_uri = models.CharField(max_length=4096)
    features = ArrayField(ArrayField(models.FloatField()))

    class Meta:
        db_table = 'feature'
