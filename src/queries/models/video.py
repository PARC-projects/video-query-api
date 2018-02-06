from django.db import models
from queries.models import Dataset


# Individual video used to as a reference of "se"search" against or reference
class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    dataset = models.ForeignKey(Dataset, related_name='videos', on_delete=models.PROTECT)
    path = models.CharField(max_length=4096, null=True)  # TODO: make required

    class Meta:
        db_table = 'video'
