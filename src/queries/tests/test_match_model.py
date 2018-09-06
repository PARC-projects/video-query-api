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
            score="0.8",
            user_match=True,
            query_result=QueryResult.objects.all()[0],
            video_clip=VideoClip.objects.all()[0]
        )

    def test_dumb(self):
        # match = Query.objects.all()[0]
        # print(match)
        self.assertTrue(True)
