from django.contrib.postgres.fields import ArrayField
from django.db import models

from . import Query


class QueryResult(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT)
    round = models.PositiveIntegerField(default=1)
    match_criterion = models.FloatField(default=0.8)
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'query_result'

    @staticmethod
    def get_latest_query_result_by_query_id(pk):
        """
        Get latest query result based on query id
        """
        return QueryResult.objects.filter(query_id=pk).last()
