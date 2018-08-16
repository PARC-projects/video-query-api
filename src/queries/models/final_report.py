from django.db import models
from . import Query


class FinalReport(models.Model):
    query = models.ForeignKey(Query, on_delete=models.PROTECT, unique=True, help_text='Query id')
    file_name = models.CharField(max_length=254, unique=True, help_text='file name for final csv report')
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    class Meta:
        db_table = 'final_reports'
