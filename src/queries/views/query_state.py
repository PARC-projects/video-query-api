from django.http import JsonResponse
from rest_framework.decorators import api_view
from queries.serializers import QuerySerializer, QueryResultSerializer, MatchSerializer, VideoSerializer
from queries.models import Query, QueryResult, Match, Video


@api_view(['GET'])
def compute_new_state(request):
    """
    GET query state that represents a new query ready to get its similarities computed
    Polled by broker in algorithm project
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_new_compute_similarity(), many=False).data
    return JsonResponse({
        "query_id": query["id"],
        "video_id": query["video"],
        "reference_time": query["reference_time"]
    })


@api_view(['GET'])
def compute_revised_state(request):
    """
    GET query state that represents a  query ready to get its similarities revised
    Polled by broker in algorithm project
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_compute_similarity(), many=False).data
    print(query)
    results = QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(query["id"]), many=False).data
    matches = MatchSerializer(Match.get_latest_matches_by_query_id(query["id"]), many=True).data
    return JsonResponse({
        "query_id": query["id"],
        "video_id": query["video"],
        "reference_time": query["reference_time"],
        "result": results,
        "matches": matches
    })
