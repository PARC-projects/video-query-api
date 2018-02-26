from django.db import models
from queries.models import Video
from django.core.exceptions import NON_FIELD_ERRORS


class VideoClip(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    clip = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(default=10)
    debug_video_uri = models.CharField(max_length=4096, null=True, blank=True)
    notes = models.TextField(max_length=25600, blank=True, null=True)

    class Meta:
        db_table = 'video_clip'
        unique_together = (('video', 'clip', 'clip_duration'),)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "(video, clip, clip_duration) in row of video_clips table is not unique.",
            }
        }
