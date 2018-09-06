from django.test import TestCase

from ..models import Query, ProcessState, SearchSet, Video


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
#     def test_dumb_test_to_insure_view_tests_are_setup_correctly(self):
#         query = Query.objects.get(name="Query 1")
#         self.assertEqual(query.name, "Query 1")
