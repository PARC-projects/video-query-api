from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from queries.models import QueryResult, Match
from queries.serializers import QueryResultSerializer


class QueryResultViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new query result instance.

    retrieve:
    Return the given query result.

    list:
    Return a list of all the existing query results.

    update:
    Update a given query result as whole.

    partial_update:
    Update a set of parameters of a given query result.
    """
    queryset = QueryResult.objects.all()
    serializer_class = QueryResultSerializer

    @action(methods=['get'], detail=True)
    def matches(self, request, pk):
        """
        GET matches based on query id.
        """
        return Response(Match.objects.filter(query_result_id=pk).values())
