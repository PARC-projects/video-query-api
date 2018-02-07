from django.db import models
from queries.models import QueryResult, Video, Query


class Match(models.Model):
    query_result = models.ForeignKey(QueryResult, on_delete=models.PROTECT)
    score = models.FloatField(default=0)
    # TODO: Remove and get from Match.score vs QueryResults.match_criterion
    is_match = models.BooleanField(default=0)
    reference_video = models.ForeignKey(Video, related_name='reference_video', on_delete=models.PROTECT)
    reference_time = models.PositiveIntegerField(default=0)
    # Holds state of user validation on UI.
    # null = they have not validated or invalidate the match
    user_match = models.NullBooleanField(default=None)

    class Meta:
        db_table = 'match'
        ordering = ('-score',)

    @staticmethod
    def get_latestest_matches_by_query_id(pk):
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
            match_entity.user_match = match['user_match'];
            match_entity.save()

        # TODO: switch 1 to enum
        Query.update_process_state_based_on_query_id(query_id, 1)
