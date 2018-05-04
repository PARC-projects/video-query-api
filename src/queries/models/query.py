from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import DateTimeField
from . import SearchSet, Video, ProcessState


class Query(models.Model):
    name = models.CharField(max_length=254, unique=True)
    search_set_to_query = models.ForeignKey(SearchSet, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    reference_time = models.DurationField(default='00:00:00')
    max_matches_for_review = models.PositiveIntegerField(default=20)
    notes = models.TextField(null=True)
    reference_clip_image = models.ImageField(null=True)
    current_round = models.PositiveIntegerField(default=1)
    current_match_criterion = models.FloatField(default=0.8)
    current_weights = ArrayField(models.FloatField(), null=True)
    process_state = models.ForeignKey(ProcessState, default=1, on_delete=models.PROTECT)
    last_modified = DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        db_table = 'query'
        ordering = ['name']

    @staticmethod
    def update_process_state_based_on_query_id(query_id, process_state):
        """
        Update processing state on Query using a query_result_id as reference
        """
        query = Query.objects.get(pk=query_id)
        query.process_state_id = process_state
        query.save()

    @staticmethod
    def get_latest_query_ready_for_compute_similarity():
        """
        Get latest query ready for revision
        :return: Query
        """
        return Query.objects.filter(process_state=2).order_by('last_modified').first()

    @staticmethod
    def get_latest_query_ready_for_new_compute_similarity():
        """
        Get latest query ready for new matches to be computed
        :return: Query
        """
        return Query.objects.filter(process_state=1).order_by('last_modified').first()
