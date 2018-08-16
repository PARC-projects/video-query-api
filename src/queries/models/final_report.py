from django.db import models
from . import Query


class FinalReport(models.Model):
    query = models.OneToOneField(Query, on_delete=models.PROTECT, primary_key=True, help_text='Query id')
    file_name = models.CharField(max_length=254, unique=True, help_text='file name for final csv report')
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        db_table = 'final_reports'

    def __str__(self):
        return "Final report for query %s" % self.query.name
