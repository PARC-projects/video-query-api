from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models

from . import VideoClip, DnnStream


class Feature(models.Model):
    video_clip = models.ForeignKey(
        VideoClip,
        on_delete=models.CASCADE,
        help_text='Id in the video_clips table for the clip corresponding to this row.'
    )
    dnn_stream = models.ForeignKey(
        DnnStream,
        to_field='type',
        on_delete=models.CASCADE,
        help_text='DNN stream name from dnn_streams table signifying which of the streams in the multi-stream DNN this '
                  'row belongs.'
    )
    dnn_stream_split = models.PositiveSmallIntegerField(
        help_text='Split number of dnn_stream, ensemble averaging is over splits of a given dnn stream.'
    )
    name = models.CharField(
        max_length=80,
        help_text='Should match the feature name in the DNN (e.g., Caffe) model.'
    )
    dnn_weights_uri = models.CharField(
        max_length=4096,
        help_text='Location of the weights file for the CNN model used to compute the feature.'
    )
    dnn_spec_uri = models.CharField(
        max_length=4096,
        null=True,
        help_text='Location of the spec for the DNN model, i.e. a prototxt file for Caffe models.'
    )
    feature_vector = ArrayField(
        models.FloatField(),
        help_text='feature vector from DNN model inference'
    )

    class Meta:
        db_table = 'feature'
        unique_together = ('video_clip', 'dnn_stream', 'dnn_stream_split', 'name')
        models.error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "(video_clip, dnn_stream, dnn_stream_split, name) is not unique."
            }
        }
