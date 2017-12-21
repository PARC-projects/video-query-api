from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Dataset(models.Model):
    name = models.CharField(max_length=254, unique=True)
    class Meta:
        db_table = 'dataset'


class Video(models.Model):
    name = models.CharField(max_length=254, unique=True)
    dataset = models.ForeignKey(Dataset, related_name='videos', on_delete=models.PROTECT)

    class Meta:
        db_table = 'video'


class Query(models.Model):
    name = models.CharField(max_length=254, unique=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    reference_time = models.TimeField(default='00:00:00')
    max_matches = models.PositiveIntegerField(default=20)
    query_notes = models.TextField()
    reference_clip_image = models.ImageField(default='Picture1.jpg' )

    class Meta:
        db_table = 'query'


class MatchedArray(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT)
    round = models.PositiveIntegerField()
    matches = ArrayField(models.PositiveIntegerField(), default=[1, 2])  # array of snippet ids
    near_matches = ArrayField(models.PositiveIntegerField(), default=[3, 4])  # array of snippet ids
    revised_matches = ArrayField(models.PositiveIntegerField(), default=[1, 2])  # array of snippet ids
    match_criterion = models.FloatField()
    near_match_criterion = models.FloatField()
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'matched_array'


class Signature(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    snippet = models.PositiveIntegerField()
    signature = ArrayField(models.FloatField())

    class Meta:
        db_table = 'signature'
