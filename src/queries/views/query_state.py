from rest_framework.decorators import api_view
from rest_framework.response import Response
from queries.serializers import QuerySerializer
from queries.models import Query


@api_view(['GET'])
def compute_similarity(request):
    # TODO: Account for empty response
    return Response(QuerySerializer(Query.get_latest_query_ready_for_compute_similarity(), many=False).data)


@api_view(['GET'])
def new_compute_similarity(request):
    # TODO: Account for empty response
    return Response(QuerySerializer(Query.get_latest_query_ready_for_new_compute_similarity(), many=False).data)
