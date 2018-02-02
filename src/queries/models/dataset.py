from django.db import models


# Identifies a collection of Videos
class Dataset(models.Model):
    name = models.CharField(max_length=254, unique=True)

    class Meta:
        db_table = 'dataset'
