from django.db import models

from . import QueryResult, Query, VideoClip, Video


class Match(models.Model):
    query_result = models.ForeignKey(QueryResult, on_delete=models.PROTECT)
    score = models.FloatField(default=0)
    # Holds state of user validation on UI.
    # null = they have not validated or invalidate the match
    user_match = models.NullBooleanField(default=None)
    video_clip = models.ForeignKey(VideoClip, on_delete=models.PROTECT)

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
        ComputeRevision = 2
        This is reached by submitting revisions on the existing query page
        """
        # TODO: CHAD - wrap in atomic transaction
        for match in matches:
            match_entity = Match.objects.get(pk=match['id'])
            match_entity.user_match = match['user_match']
            match_entity.save()

        # TODO: CHAD - switch to enum
        Query.update_process_state_based_on_query_id(query_id, 2)

    @property
    def query_id(self):
        return QueryResult.objects.values_list('query', flat=True).get(id=self.query_result_id)

    # TODO: CHAD: Check with Frank to see where he is using this.
    @property
    def reference_video_id(self):
        return Query.objects.values_list('video', flat=True).get(id=self.query_id)

    # TODO: CHAD: Check with Frank to see where he is using this.
    @property
    def reference_time(self):
        return Query.objects.values_list('reference_time', flat=True).get(id=self.query_id)

    @property
    def match_video_path(self):
        """
        TODO: CHAD - Consider perf of multiple calls to VideoClip.
        Used on UI to show video for match (../existing-query)
        :return:
        Location of video this match is associated with.
        """
        video_id = VideoClip.objects.values_list('video', flat=True).get(id=self.video_clip_id)
        return Video.objects.values_list('path', flat=True).get(id=video_id)

    @property
    def match_video_start_time(self):
        """
        TODO: CHAD - Consider perf of multiple calls to VideoClip.
        Used on UI to calc reference time for matching video (../existing-query)
        :return:
        Location of video this match is associated with.
        """
        clip = VideoClip.objects.get(id=self.video_clip_id)
        return clip.duration * clip.clip

    @property
    def is_match(self):
        match_criterion = QueryResult.objects.values_list('match_criterion', flat=True).get(id=self.query_result_id)
        return self.score >= match_criterion
