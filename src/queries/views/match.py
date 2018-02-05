from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
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
def match_list(request):
    """
    API endpoint to perform list based operations on matches
    """
    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        match = Match.patch_list_of_matches(data)
        return JsonResponse('ok', safe=False)
