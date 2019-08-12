from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    path = models.CharField(max_length=4096)
    web_source = models.BooleanField(default=False)

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.name
