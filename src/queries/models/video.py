from django.db import models
from queries.models import SearchSet


class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    search_sets = models.ManyToManyField(SearchSet)
    path = models.CharField(max_length=4096)

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.name
