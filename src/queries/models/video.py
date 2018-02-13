from django.db import models
from queries.models import SearchSet


class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    # TODO: drop in favor of Video <=> SearchSet table
    # dataset = models.ForeignKey(SearchSet, related_name='videos', on_delete=models.PROTECT)
    search_set = models.ManyToManyField(SearchSet)
    path = models.CharField(max_length=4096, null=True)  # TODO: make required

    class Meta:
        db_table = 'video'
