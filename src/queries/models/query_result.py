from django.db import models
from django.contrib.postgres.fields import ArrayField
from queries.models import Query


class QueryResult(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT)
    round = models.PositiveIntegerField(default=1)
    match_criterion = models.FloatField(default=0.8)
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'query_result'

    def get_latestest_query_result_by_query_id(self, pk):
        """
        Get latest query result based on query id
        """
        return QueryResult.objects.filter(query_id=pk).last()
