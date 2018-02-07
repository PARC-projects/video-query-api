from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from queries.models import Match
from queries.serializers import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows match to be viewed or edited.
    <br/>
    <br/>
    <b>matches_list</b>
    <ul>
        <li>PATCH: Update a collection of matches</li>
    </ul>
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


@csrf_exempt
@api_view(['PATCH'])
def match_list(request):
    """
    API endpoint to perform list based operations on matches
    """
    if request.method == 'PATCH':
        data = JSONParser().parse(request)

        # No need to process transaction if we don't have matches
        if len(data) < 1:
            return Response(status=status.HTTP_204_NO_CONTENT)

        Match.patch_list_of_matches(data['matches'], data['query_id'])
        return Response(status=status.HTTP_204_NO_CONTENT)
