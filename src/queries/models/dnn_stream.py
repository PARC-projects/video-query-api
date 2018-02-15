from django.db import models


class DnnStream(models.Model):
    type = models.CharField(max_length=80, unique=True)
    max_number_of_splits = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'dnn_streams'
