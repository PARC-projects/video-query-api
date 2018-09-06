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

        Query.objects.create(
            name="Query 1",
            search_set_to_query_id=1,
            video_id=1,
            process_state=ProcessState.objects.get(name="Process State 1")
        )

        QueryResult.objects.create(
            query=Query.objects.all()[0],
            round=1,
            match_criterion=0.8,
            weights=[1]
        )

        Video.objects.create(
            name="video 1",
            path="src/path"
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
        match = Query.objects.all()[0]
        print(match)
        self.assertTrue(True)

# class QueryTest(TestCase):
#     """ Test module for Query model """
#
#     def setUp(self):
#
#         ProcessState.objects.create(
#             name="Process State 1"
#         )
#
#         SearchSet.objects.create(
#             name="Search Set 1",
#             duration=10
#         )
#
#         Video.objects.create(
#             name="Video 1",
#             path="high"
#         )
#
#         Query.objects.create(
#             name="Query 1",
#             search_set_to_query_id=1,
#             video_id=1,
#             process_state=ProcessState.objects.get(name="Process State 1")
#         )
#
#     def test_dumb_test_to_insure_model_tests_are_setup_correctly(self):
#         query = Query.objects.get(name="Query 1")
#         self.assertEqual(query.name, "Query 1")
