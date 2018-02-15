from django.db import models

from queries.models import Video


class VideoClip(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    clip = models.PositiveIntegerField();
    duration = models.PositiveIntegerField(default=10);
    debug_video_uri = models.CharField(max_length=4096, null=True)
    notes = models.TextField(null=True)

    class Meta:
        db_table = 'video_clip'
