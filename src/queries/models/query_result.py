from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS

from . import Query


class QueryResult(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT)
    round = models.PositiveIntegerField(default=1)
    match_criterion = models.FloatField(default=0.8)
    weights = ArrayField(models.FloatField())

    class Meta:
        db_table = 'query_result'
        unique_together = ('query', 'round')
        models.error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "(query, round) is not unique in query_results table."
            }
        }

    @staticmethod
    def get_latest_query_result_by_query_id(pk):
        """
        Get latest query result based on query id
        """
        results = QueryResult.objects.filter(query_id=pk)
        if len(results) > 0:
            return QueryResult.objects.filter(query_id=pk).order_by('-round').values()[0]
        return None
