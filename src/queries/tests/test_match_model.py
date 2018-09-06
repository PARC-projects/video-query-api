from django.test import TestCase
from ..models import Query, ProcessState, SearchSet, Video, Match, QueryResult, VideoClip


class MatchTest(TestCase):
    """ Test module for Match model """

    def setUp(self):
        ProcessState.objects.create(
            name="Process State 1"
        )

        SearchSet.objects.create(
            name="Search Set 1",
            duration=10
        )

        Video.objects.create(
            name="video 1",
            path="src/path"
        )

        Query.objects.create(
            name="Query 1",
            search_set_to_query_id=SearchSet.objects.all()[0].id,
            video_id=Video.objects.all()[0].id,
            process_state=ProcessState.objects.all()[0]
        )

        QueryResult.objects.create(
            query=Query.objects.all()[0],
            round=1,
            match_criterion=0.8,
            weights=[1]
        )

        VideoClip.objects.create(
            video=Video.objects.all()[0],
            clip=1,
            duration=10
        )

        Match.objects.create(
            score="0.7",
            user_match=True,
            query_result=QueryResult.objects.all()[0],
            video_clip=VideoClip.objects.all()[0]
        )

        Match.objects.create(
            score="0.9",
            user_match=True,
            query_result=QueryResult.objects.all()[0],
            video_clip=VideoClip.objects.all()[0]
        )

    def test_is_match_equals_false_when_score_is_below_match_criterion(self):
        match = Match.objects.all()[0]
        self.assertTrue(match.is_match)

    def test_is_match_equals_false_when_score_is_below_match_criterion(self):
        match = Match.objects.all()[1]
        self.assertFalse(match.is_match)

    def test_match_video_time_span_is_formatted_as_comma_separated(self):
        match = Match.objects.all()[0]
        clip = VideoClip.objects.get(id=match.video_clip_id)
        self.assertEqual(
            match.match_video_time_span,
            "{},{}".format(clip.duration * (clip.clip - 1), clip.duration * clip.clip)
        )

    def test_match_video_time_span_start(self):
        match = Match.objects.all()[0]
        clip = VideoClip.objects.get(id=match.video_clip_id)

        words = clip.match_video_time_span.split(",")

        self.assertEqual(clip.duration * (clip.clip - 1), words[0], "video_time_span has an inaccurate start")

    def test_match_video_time_span_end(self):
        match = Match.objects.all()[0]
        clip = VideoClip.objects.get(id=match.video_clip_id)

        words = clip.match_video_time_span.split(",")

        self.assertEqual(clip.duration * clip.clip, words[1])
