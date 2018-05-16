from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from queries.models import Query, QueryResult, Match, SearchSet, VideoClip
from queries.serializers import QuerySerializer, QueryResultSerializer, MatchSerializer


@api_view(['GET'])
def compute_new_state(request):
    """ GET - Get query state that represents a new query ready to get its similarities computed.
    <ul>
        <li>Polled by broker in algorithm project.</li>
        <li>
            <a href="https://github.com/PARC-projects/video-query-api/blob/master/src/queries/models/process_state.py">
                Processing State
            </a> == 1
        </li>
    </ul>
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_new_matches(), many=False).data
    if 'id' in query:
        clip_duration = SearchSet.objects.get(id=query["search_set_to_query"]).duration
        ref_time = Query.objects.get(id=query["id"]).reference_time
        ref_clip = int(ref_time.total_seconds() / clip_duration) + 1
        ref_clip_id = VideoClip.objects.get(clip=ref_clip, video=query["video"], duration=clip_duration).id
        search_set = SearchSet.objects.get(query=query["id"]).id
        number_of_matches = Query.objects.get(id=query["id"]).max_matches_for_review
        current_round = Query.objects.get(id=query["id"]).current_round
        return JsonResponse({
            "query_id": query["id"],
            "video_id": query["video"],
            "ref_clip": ref_clip,
            "ref_clip_id": ref_clip_id,
            "search_set": search_set,
            "number_of_matches_to_review": number_of_matches,
            "current_round": current_round
        })

    return Response("No new queries were found.", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def compute_revised_state(request):
    """ GET - Get query state that represents a query ready to get its similarities revised.
    <ul>
        <li>Polled by broker in algorithm project.</li>
        <li>
            <a href="https://github.com/PARC-projects/video-query-api/blob/master/src/queries/models/process_state.py">
                Processing State
            </a> == 2
        </li>
    </ul>
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_revision(), many=False).data
    if 'id' in query:
        results = QueryResultSerializer(QueryResult.get_latest_query_result_by_query_id(query["id"]),
                                        many=False).data
        matches = MatchSerializer(Match.get_latest_matches_by_query_id(query["id"]), many=True).data
        clip_duration = SearchSet.objects.get(id=query["search_set_to_query"]).duration
        ref_time = Query.objects.get(id=query["id"]).reference_time
        ref_clip = int(ref_time.total_seconds() / clip_duration) + 1
        ref_clip_id = VideoClip.objects.get(clip=ref_clip, video=query["video"], duration=clip_duration).id
        search_set = SearchSet.objects.get(query=query["id"]).id
        number_of_matches = Query.objects.get(id=query["id"]).max_matches_for_review
        current_round = Query.objects.get(id=query["id"]).current_round
        return JsonResponse({
            "query_id": query["id"],
            "video_id": query["video"],
            "ref_clip": ref_clip,
            "ref_clip_id": ref_clip_id,
            "result": results,
            "matches": matches,
            "search_set": search_set,
            "number_of_matches_to_review": number_of_matches,
            "current_round": current_round
        })

    return Response("No revised queries were found.", status=status.HTTP_204_NO_CONTENT)
