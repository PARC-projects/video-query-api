from django.db import models


# Identifies a collection of videos
class SearchSet(models.Model):
    name = models.CharField(max_length=254, unique=True)

    class Meta:
        db_table = 'search_set'
