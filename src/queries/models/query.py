from django.db import models
from django.db.models import DateTimeField

from . import SearchSet, Video, ProcessState, VideoClip

''' for storing files in user-specific directories when we get to that point
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'final_reports/user_{0}/{1}'.format(instance.user.id, filename)
    
    and change to upload_to=user_directory_path
'''


class Query(models.Model):
    name = models.CharField(max_length=254, unique=True)
    search_set_to_query = models.ForeignKey(SearchSet, on_delete=models.PROTECT)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
    reference_time = models.DurationField(default='00:00:00')
    max_matches_for_review = models.PositiveIntegerField(default=20)
    notes = models.TextField(null=True)
    reference_clip_image = models.ImageField(null=True)
    process_state = models.ForeignKey(ProcessState, default=1, on_delete=models.PROTECT)
    final_report_file = models.FileField(max_length=254, upload_to='final_reports/', null=True,
                                         help_text='final csv report. For coreapi, use encoding in client.action(): '
                                                   'client.action(..., encoding="multipart/form-data")')
    last_modified = DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    # Let the algorithms know whether to “average” the features of all validated matches in each round and have that be
    # the new reference.
    use_dynamic_target_adjustment = models.BooleanField(default=False)

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
    def get_latest_query_ready_for_revision():
        """
        Get latest query ready for revision
        :return: Query
        """
        return Query.objects.filter(process_state=2).order_by('last_modified').first()

    @staticmethod
    def get_latest_query_ready_for_new_matches():
        """
        Get latest query ready for new matches to be computed
        :return: Query
        """
        return Query.objects.filter(process_state=1).order_by('last_modified').first()

    @staticmethod
    def get_latest_query_ready_for_finalize():
        """
        Get latest query ready to be finalized
        :return: Query
        """
        return Query.objects.filter(process_state=6).order_by('last_modified').first()

    @property
    def reference_clip_number(self):
        return int(self.reference_time.total_seconds() / self.clip_duration) + 1

    @property
    def reference_clip_pk(self):
        ref_clip = VideoClip.objects\
            .get(video_id=self.video_id, clip=self.reference_clip_number, duration=self.clip_duration)
        if ref_clip:
            return ref_clip.id
        return None

    @property
    def clip_duration(self):
        return SearchSet.objects.values_list('duration', flat=True).get(id=self.search_set_to_query_id)

    @property
    def final_report_url(self):
        return self.final_report_file.url
