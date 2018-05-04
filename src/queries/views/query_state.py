from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from queries.serializers import QuerySerializer, QueryResultSerializer, MatchSerializer
from queries.models import Query, QueryResult, Match, SearchSet, VideoClip
from rest_framework import status


@api_view(['GET'])
def compute_new_state(request):
    """
    GET query state that represents a new query ready to get its similarities computed
    Polled by broker in algorithm project
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_new_compute_similarity(), many=False).data
    if 'id' in query:
        clip_duration = SearchSet.objects.get(id=query["search_set_to_query"]).duration
        ref_time = Query.objects.get(id=query["id"]).reference_time
        ref_clip = int(ref_time.total_seconds() / clip_duration) + 1
        ref_clip_id = VideoClip.objects.get(clip=ref_clip, video=query["video"], duration=clip_duration).id
        return JsonResponse({
            "query_id": query["id"],
            "video_id": query["video"],
            "ref_clip_id":ref_clip_id
        })

    return Response("No new queries were found.", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def compute_revised_state(request):
    """
    GET query state that represents a  query ready to get its similarities revised
    Polled by broker in algorithm project
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_compute_similarity(), many=False).data
    if 'id' in query:
        results = QueryResultSerializer(QueryResult.get_latestest_query_result_by_query_id(query["id"]),
                                        many=False).data
        matches = MatchSerializer(Match.get_latest_matches_by_query_id(query["id"]), many=True).data
        clip_duration = SearchSet.objects.get(id=query["search_set_to_query"]).duration
        ref_time = Query.objects.get(id=query["id"]).reference_time
        ref_clip = int(ref_time.total_seconds() / clip_duration) + 1
        ref_clip_id = VideoClip.objects.get(clip=ref_clip, video=query["video"], duration=clip_duration).id
        return JsonResponse({
            "query_id": query["id"],
            "video_id": query["video"],
            "ref_clip_id": ref_clip_id,
            "result": results,
            "matches": matches
        })

    return Response("No revised queries were found.", status=status.HTTP_204_NO_CONTENT)
