from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from queries.serializers import QuerySerializer, QueryResultSerializer, MatchSerializer, VideoSerializer
from queries.models import Query, QueryResult, Match, Video


class QueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows queries to be viewed or edited.
    <br/>
    <b>queries/{id}/query_result</b>: GET latest query result based on query id
    <br/>
    <b>queries/{id}/matches</b>: GET latest matches based on query id
    <br/>
    <b>queries/{id}/compute_new_state</b>: GET query state that represents a new query ready to get its similarities computed
    <br/>
    <b>queries/{id}/compute_revised_state</b>: GET query state that represents a query ready to get its similarities revised
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    @detail_route(methods=['get'])
    def query_result(self, request, pk):
        """
        GET Latest QueryResult base on Query Id
        :param request:
        :param pk: Query Id
        :return: QueryResult
        """
        return Response(QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(pk), many=False).data)

    @detail_route(methods=['get'])
    def matches(self, request, pk):
        """
        GET latest Match(s) based on Query Id
        :param request:
        :param pk: Query Id
        :return: Match[]
        """
        return Response(MatchSerializer(Match.get_latestest_matches_by_query_id(pk), many=True).data)

    @detail_route(methods=['get'])
    def compute_new_state(self, request, pk):
        """
        GET query state that represents a new query ready to get its similarities computed
        Polled by broker in algorithm project
        :param request:
        :param pk:
        :return:
        """
        query = QuerySerializer(Query.get_latest_query_ready_for_new_compute_similarity(), many=False).data
        results = QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(pk), many=False).data
        return JsonResponse({
            "query_id": pk,
            "video_id": query["video"],
            "reference_time": query["reference_time"],
            "results": results
        })

    @detail_route(methods=['get'])
    def compute_revised_state(self, request, pk):
        """
        GET query state that represents a  query ready to get its similarities revised
        Polled by broker in algorithm project
        :param request:
        :param pk: Query Id
        :return:
        """
        query = QuerySerializer(Query.get_latest_query_ready_for_compute_similarity(), many=False).data
        results = QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(pk), many=False).data
        matches = MatchSerializer(Match.get_latestest_matches_by_query_id(pk), many=True).data
        return JsonResponse({
            "query_id": pk,
            "video_id": query["video"],
            "reference_time": query["reference_time"],
            "results": results,
            "matches": matches
        })
