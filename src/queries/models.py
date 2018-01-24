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
    path = models.CharField(max_length=4096, null=True)  # TODO: make required

    class Meta:
        db_table = 'video'


class Query(models.Model):
    name = models.CharField(max_length=254, unique=True)
    dataset_to_query = models.ForeignKey(Dataset, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    reference_time = models.TimeField(default='00:00:00')
    max_matches_for_review = models.PositiveIntegerField(default=20)
    query_notes = models.TextField(null=True)
    reference_clip_image = models.ImageField(null=True)
    current_round = models.PositiveIntegerField(default=1)
    current_match_criterion = models.FloatField(default=0.8)
    current_weights = ArrayField(models.FloatField(), null=True)

    class Meta:
        db_table = 'query'
        ordering = ['-id']

    def get_latestest_query_result_by_query_id(self, pk):
        """
        Get latest query result based on query id
        """
        return QueryResult.objects.filter(query_id=pk).last()

    def get_latestest_matches_by_query_id(self, pk):
        """
        Get latest matches based on query id
        """
        result = QueryResult.objects.filter(query_id=pk).last()
        if result == None:
            return None
        else:
            return Match.objects.filter(query_result=result.id)


class QueryResult(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT)
    round = models.PositiveIntegerField(default=1)
    match_criterion = models.FloatField(default=0.8)
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'query_result'


class Match(models.Model):
    query_result = models.ForeignKey(QueryResult, on_delete=models.PROTECT)
    score = models.FloatField(default=0)
    is_match = models.BooleanField(default=0)
    reference_video = models.ForeignKey(Video, related_name='reference_video', on_delete=models.PROTECT)
    reference_time = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'match'
        ordering = ('-score',)

    def get_latest_matches_by_query_id(self, pk):
        """
        Get latest query result based on query id
        """
        latest = QueryResult.get_latestest_query_result(self, pk)

        return Match.objects.filter(query_result_id=latest.round).values()


class Signature(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    snippet = models.PositiveIntegerField()
    signature = ArrayField(models.FloatField())

    class Meta:
        db_table = 'signature'
