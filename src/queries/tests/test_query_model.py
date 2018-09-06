from django.test import TestCase

from ..models import Query, ProcessState, SearchSet, Video


class QueryTest(TestCase):
    """ Test module for Query model """

    def setUp(self):
        ProcessState.objects.create(
            name="Process State 1"
        )

        SearchSet.objects.create(
            name="Search Set 1",
            duration=10
        )

        Video.objects.create(
            name="Video 1",
            path="high"
        )

        Query.objects.create(
            name="Query 1",
            search_set_to_query_id=SearchSet.objects.all()[0].id,
            video_id=Video.objects.all()[0].id,
            process_state=ProcessState.objects.all()[0]
        )

        Query.objects.create(
            name="Query 2",
            search_set_to_query_id=SearchSet.objects.all()[0].id,
            video_id=Video.objects.all()[0].id,
            process_state=ProcessState.objects.all()[0],
            final_report_file='final_reports/final_report_query_14_08-18-2018_10h23m34s.csv'

        )

    def test_reference_clip_number(self):
        query = Query.objects.get(name="Query 1")

        self.assertEqual(
            query.reference_clip_number,
            int(query.reference_time.total_seconds() / query.clip_duration) + 1,
            "test_reference_clip_number: Reference Clip Number was not calculated correctly"
        )

    def test_final_report_url_is_null_when_no_final_report_is_available(self):
        query = Query.objects.get(name="Query 1")

        self.assertEqual(query.final_report_url, None)

    def test_final_report_url_is_valid_rul_when_final_report_is_available(self):
        query = Query.objects.get(name="Query 2")

        self.assertIsNotNone(query.final_report_url)

