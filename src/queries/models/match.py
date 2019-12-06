import time

from django.db import models

from . import QueryResult, Query, VideoClip, Video


class Match(models.Model):
    query_result = models.ForeignKey(QueryResult, on_delete=models.CASCADE)
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
        result = QueryResult.get_latest_query_result_by_query_id(pk)
        if result is None:
            return None
        else:
            return Match.objects.filter(query_result=result["id"])

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

    @property
    def reference_video_id(self):
        return Query.objects.values_list('video', flat=True).get(id=self.query_id)

    @property
    def reference_video_external_source(self):
        """
        Identifies if realted video is of external source
        """
        video_id = VideoClip.objects.values_list(
            'video', flat=True).get(id=self.video_clip_id)
        return Video.objects.values_list('external_source', flat=True).get(id=video_id)

    @property
    def reference_time(self):
        return Query.objects.values_list('reference_time', flat=True).get(id=self.query_id)

    @property
    def match_video_path(self):
        """
        TODO: CHAD - Consider perf of multiple calls to VideoClip.
        Used on UI to show video for match (../existing-query)`
        :return:
        Location of video this match is associated with.
        """
        video_id = VideoClip.objects.values_list(
            'video', flat=True).get(id=self.video_clip_id)
        return Video.objects.values_list('path', flat=True).get(id=video_id)

    @property
    def match_video_time_span(self):
        """
        TODO: CHAD - Consider perf of multiple calls to VideoClip.
        Used on UI to calc reference time for matching video (../existing-query)
        :return:
        Location of video this match is associated with.
        """
        clip = VideoClip.objects.get(id=self.video_clip_id)
        return "{},{}".format(self.__get_video_time_span_start(clip), self.__get_video_time_span_end(clip))

    @property
    def is_match(self):
        match_criterion = QueryResult.objects.values_list(
            'match_criterion', flat=True).get(id=self.query_result_id)
        return self.score >= match_criterion

    @property
    def match_video_name(self):
        """
        TODO: CHAD - Consider perf of multiple calls to VideoClip.
        Used on UI to show video for match (../existing-query)`
        :return:
        Location of video this match is associated with.
        """
        video_id = VideoClip.objects.values_list(
            'video', flat=True).get(id=self.video_clip_id)
        return Video.objects.values_list('name', flat=True).get(id=video_id)

    @property
    def reference_start_time(self):
        """
        Format a reference start time so we can set video position on UI.
        """
        return time.strftime('%H:%M:%S', time.gmtime(int(self.match_video_time_span.split(',')[0])))

    @property
    def reference_end_time(self):
        """
        Format a reference end time so we can set video position on UI.
        """
        return time.strftime('%H:%M:%S', time.gmtime(int(self.match_video_time_span.split(',')[1])))

    @staticmethod
    def __get_video_time_span_start(clip):
        """
        Get the start time of a video time span based on clip
        """
        return clip.duration * (clip.clip - 1)

    @staticmethod
    def __get_video_time_span_end(clip):
        """
        Get the end time of a video time span based on clip
        """
        return clip.duration * clip.clip
