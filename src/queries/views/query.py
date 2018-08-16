from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from queries.models import Query, QueryResult, Match
from queries.serializers import QuerySerializer, MatchSerializer


class QueryViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new query instance. <br/>
    A query's video is divided into clips 1, 2, 3, ... <br/>
    Reference clip number is the clip containing the reference time. <br/>
    Dynamic target adjustment is when the target features are adjusted to
    an average for the population of validated matches in each round.

    retrieve:
    Return the given query. <br/>

    list:
    Return a list of all the existing queries. <br/>
    Search term: query name

    update:
    Update a given query as whole.

    partial_update:
    Update a set of parameters of a given query.
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filter_fields = ('name',)

    @action(methods=['get'], detail=True)
    def query_result(self, request, pk):
        """
        GET Latest QueryResult base on Query Id
        """
        return Response(QueryResult.get_latest_query_result_by_query_id(pk))

    @action(methods=['get'], detail=True)
    def matches(self, request, pk):
        """
        GET latest Match(s) based on Query Id
        """
        return Response(MatchSerializer(Match.get_latest_matches_by_query_id(pk), many=True).data)
