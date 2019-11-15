from django.db import models


class ProcessState(models.Model):
    """
        if 1: ComputeNew (Submitted)
            UI - New query was submitted and initial set of matches need to be computed.
            Daemon - Will grab latest query in this state
            ML - Will be told to execute against this query
        if 2: ComputeRevision (Revised)
            UI - A revision has been submitted and weights need to be optimized
            Daemon - Will grab latest query in this state
            ML - If similarities are not cached, will need to recompute them.
                    When similarities are cached, optimize weights
        if 3: Processing (Processing)
            UI - show "check back soon" state
            Daemon - nothing
            ML - is processing
        if 4: Processed (Processed)
            UI - Allows for re-submission of query
            Daemon - nothing
            ML - Sets to this state when done processing
        if 5: Error state (Error)
            The query is invalid, e.g. there is no video clip in the database for
            the specified reference time.
        if 6: Ready to be Finalized (ProcessFinalized)
            User has requested query to be Finalized from UI.
            Broker passes state to algo pipeline.
            Algo pipeline produces finalized assets.
        if 7: Finalized (Finalized)
            UI - shows link to csv file with final results
            Daemon - nothing
            ML - Sets to this state when done finalizing

    """
    name = models.CharField(max_length=254, unique=True, editable=False)

    class Meta:
        db_table = 'process_state'
