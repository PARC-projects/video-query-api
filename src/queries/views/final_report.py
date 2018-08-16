from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from queries.models import FinalReport
from queries.serializers import FinalReportSerializer


class FinalReportViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new final report instance.

    retrieve:
    Return the given final report record.

    list:
    Return a list of all the existing final report records.<br/>
    Search term: report name and/or query

    update:
    Update a given final report instance as whole.

    partial_update:
    Update a set of parameters of a final report entity.
    """
    queryset = FinalReport.objects.all()
    serializer_class = FinalReportSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('query', 'file_name')
    filter_fields = ('query', 'file_name')
