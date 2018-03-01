from django.db import models


class DnnStream(models.Model):
    type = models.CharField(max_length=80, unique=True)
    max_number_of_splits = models.PositiveSmallIntegerField(blank=True, null=True,
                                                    help_text='maximum allowed number of splits for this stream')

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'dnn_streams'
