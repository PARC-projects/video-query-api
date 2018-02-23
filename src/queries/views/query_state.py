from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from queries.serializers import  QueryResultSerializer, MatchSerializer
from queries.models import  QueryResult, Match


class QueryState(APIView):
    """
    API endpoint that allows queries to be viewed or edited.
    """

    @detail_route(methods=['get'])
    def compute_similarity(self, request, pk):
        return Response(QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(pk), many=False).data)

    @detail_route(methods=['get'])
    def new_compute_similarity(self, request, pk):
        return Response(MatchSerializer(Match.get_latestest_matches_by_query_id(pk), many=True).data)
