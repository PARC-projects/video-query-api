from django.db import models

from . import QueryResult, Query


class Match(models.Model):
    query_result = models.ForeignKey(QueryResult, on_delete=models.PROTECT)
    score = models.FloatField(default=0)
    # Holds state of user validation on UI.
    # null = they have not validated or invalidate the match
    user_match = models.NullBooleanField(default=None)

    class Meta:
        db_table = 'match'
        ordering = ('-score',)

    @staticmethod
    def get_latest_matches_by_query_id(pk):
        """
        Get latest matches based on query id
        """
        result = QueryResult.objects.filter(query_id=pk).last()
        if result is None:
            return None
        else:
            return Match.objects.filter(query_result=result.id)

    @staticmethod
    def patch_list_of_matches(matches, query_id):
        """
        Guarded updates on user validation "user_match"
        Process switch = Submitted = 1
        """
        # TODO: wrap in atomic transaction
        for match in matches:
            match_entity = Match.objects.get(pk=match['id'])
            match_entity.user_match = match['user_match']
            match_entity.save()

        # TODO: switch 1 to enum
        Query.update_process_state_based_on_query_id(query_id, 1)

    @property
    def query_id(self):
        return QueryResult.objects.values_list('query', flat=True).get(id=self.query_result_id)

    @property
    def reference_video_id(self):
        return Query.objects.values_list('video', flat=True).get(id=self.query_id)

    @property
    def reference_time(self):
        return Query.objects.values_list('reference_time', flat=True).get(id=self.query_id)

    @property
    def is_match(self):
        match_criterion = QueryResult.objects.values_list('match_criterion', flat=True).get(id=self.query_result_id)
        return self.score >= match_criterion
