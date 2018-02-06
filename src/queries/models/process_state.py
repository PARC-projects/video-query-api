from django.db import models


class ProcessState(models.Model):
    # If "Submitted" = 1
    # - UI shows "check back soon" state
    # - ML service start a new process loop and sets value to "Processing".
    # If "Processing" = 2
    # - UI shows "check back soon" state
    # - ML processes query
    # If "Processed" = 3
    # - UI allows for resubmission of query
    # - ML service does nothing
    name = models.CharField(max_length=254, unique=True)

    class Meta:
        db_table = 'process_state'
