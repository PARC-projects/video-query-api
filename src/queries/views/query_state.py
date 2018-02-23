from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.views import APIView

from queries.serializers import QuerySerializer
from queries.models import Query


class QueryState(APIView):
    """
    API endpoint that allows queries to be viewed or edited.
    """

    @detail_route(methods=['get'])
    def compute_similarity(self, request):
        return Response(QuerySerializer(Query.get_latest_query_ready_for_compute_similarity()).data)

    @detail_route(methods=['get'])
    def new_compute_similarity(self, request):
        return Response(QuerySerializer(Query.get_latest_query_ready_for_new_compute_similarity()).data)
