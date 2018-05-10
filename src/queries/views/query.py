from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from queries.models import Query, QueryResult, Match
from queries.serializers import QuerySerializer, QueryResultSerializer, MatchSerializer


class QueryViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new query instance.

    retrieve:
    Return the given query.

    list:
    Return a list of all the existing queries.
    Search term: query name

    update:
    Update a given query as whole.

    partial_update:
    Update a set of parameters of a given query.
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    @action(methods=['get'], detail=True)
    def query_result(self, request, pk):
        """
        GET Latest QueryResult base on Query Id
        """
        return Response(QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(pk), many=False).data)

    @action(methods=['get'], detail=True)
    def matches(self, request, pk):
        """
        GET latest Match(s) based on Query Id
        """
        return Response(MatchSerializer(Match.get_latest_matches_by_query_id(pk), many=True).data)
