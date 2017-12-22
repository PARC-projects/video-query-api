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
    path = models.CharField(max_length=4096, blank=True) # TODO: make required

    class Meta:
        db_table = 'video'


class Query(models.Model):
    name = models.CharField(max_length=254, unique=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    reference_time = models.TimeField(default='00:00:00')
    max_matches = models.PositiveIntegerField(default=20)
    query_notes = models.TextField(blank=True)
    reference_clip_image = models.ImageField(blank=True)
    current_round = models.PositiveIntegerField(default=1)
    current_match_criterion = models.FloatField(default=0.8)
    current_weights = ArrayField(models.FloatField(), blank=True)

    class Meta:
        db_table = 'query'


class QueryResult(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT)
    matches = ArrayField(models.PositiveIntegerField())
    round = models.PositiveIntegerField(default=1)
    score = models.FloatField(default=0)
    is_match = models.BooleanField(default=0)
    match_criterion = models.FloatField(default=0.8)
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'query_result'


class Signature(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    snippet = models.PositiveIntegerField()
    signature = ArrayField(models.FloatField())

    class Meta:
        db_table = 'signature'
