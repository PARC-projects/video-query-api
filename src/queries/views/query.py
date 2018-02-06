from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from queries.serializers import QuerySerializer, QueryResultSerializer, MatchSerializer
from queries.models import Query, QueryResult, Match


class QueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows queries to be viewed or edited.
    <br/>
    <b>queries/{id}/query_result</b>: GET latest query result based on query id
    <br/>
    <b>queries/{id}/matches</b>: GET latest matches based on query id
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    @detail_route(methods=['get'])
    def query_result(self, request, pk):
        return Response(QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(self, pk), many=False).data)

    @detail_route(methods=['get'])
    def matches(self, request, pk):
        return Response(MatchSerializer(Match.get_latestest_matches_by_query_id(pk), many=True).data)
