from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    path = models.CharField(max_length=4096)
    external_source = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    length_in_seconds = models.PositiveIntegerField()

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.name
