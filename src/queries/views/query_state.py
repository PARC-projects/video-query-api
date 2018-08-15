from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from queries.models import Query, QueryResult, Match, SearchSet, VideoClip
from queries.serializers import QuerySerializer, MatchSerializer


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
        return JsonResponse(_get_base_state_entity(query))
    else:
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
        results = QueryResult.get_latest_query_result_by_query_id(query["id"])
        matches = MatchSerializer(Match.get_latest_matches_by_query_id(query["id"]), many=True).data
        base = _get_base_state_entity(query)
        base.update(_get_revision_update(query))
        return JsonResponse(base)
    else:
        return Response("No revised queries were found.", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def compute_finalized_state(request):
    """ GET - Get query state that represents a query ready to be finalized
    <ul>
        <li>Polled by broker in algorithm project.</li>
        <li>
            <a href="https://github.com/PARC-projects/video-query-api/blob/master/src/queries/models/process_state.py">
                Processing State
            </a> == 6
        </li>
    </ul>
    """
    query = QuerySerializer(Query.get_latest_query_ready_for_finalize(), many=False).data
    if 'id' in query:
        base = _get_base_state_entity(query)
        base.update(_get_revision_update(query))
        return JsonResponse(base)
    else:
        return Response("No queries to be finalized were found.", status=status.HTTP_204_NO_CONTENT)


def _get_base_state_entity(query):
    """ Get meta information that supports a State entity being sent downstream to algo-calc
    """
    ref_clip = Query.objects.get(id=query["id"]).reference_clip_number
    try:
        ref_clip_id = Query.objects.get(id=query["id"]).reference_clip_pk
    except VideoClip.DoesNotExist:
        ref_clip_id = None
    search_set = SearchSet.objects.get(query=query["id"]).id
    number_of_matches = Query.objects.get(id=query["id"]).max_matches_for_review
    dynamic_target_adjustment = Query.objects.get(id=query["id"]).use_dynamic_target_adjustment
    return {
        "query_id": query["id"],
        "video_id": query["video"],
        "ref_clip": ref_clip,
        "ref_clip_id": ref_clip_id,
        "search_set": search_set,
        "number_of_matches_to_review": number_of_matches,
        "dynamic_target_adjustment": dynamic_target_adjustment
    }


def _get_revision_update(query):
    results = QueryResult.get_latest_query_result_by_query_id(query["id"])
    matches = MatchSerializer(Match.get_latest_matches_by_query_id(query["id"]), many=True).data
    return {"tuning_update": results, "matches": matches}
