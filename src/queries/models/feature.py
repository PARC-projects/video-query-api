from django.db import models
from django.contrib.postgres.fields import ArrayField

from queries.models import VideoClip, DnnStream


class Feature(models.Model):
    video_clip = models.ForeignKey(VideoClip, on_delete=models.PROTECT, null=True)  # TODO: Make non-nullable
    dnn_stream = models.ForeignKey(DnnStream, on_delete=models.PROTECT, null=True)  # TODO: Make non-nullable
    dnn_stream_split = models.PositiveSmallIntegerField(null=True)  # TODO: Make non-nullable
    name = models.CharField(max_length=80, null=True)  # TODO: Make non-nullable
    weights_uri = models.CharField(max_length=4096, null=True)  # TODO: Make non-nullable
    dnn_spec_uri = models.CharField(max_length=4096, null=True)
    features = ArrayField(ArrayField(models.FloatField()), null=True)  # TODO: Make non-nullable

    class Meta:
        db_table = 'feature'
