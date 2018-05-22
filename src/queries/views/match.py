from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from queries.models import Match
from queries.serializers import MatchSerializer


class MatchViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new match instance.

    retrieve:
    Return the given match.

    list:
    Return a list of all the existing matches.

    update:
    Update a given match as whole.

    partial_update:
    Update a set of parameters of a given match.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


@csrf_exempt
@api_view(['PATCH'])
def match_list(request):
    """
    Update a set of parameters of a given match in a collection (partial_updates).
    This is reached by submitting revisions on the existing query page
    """
    if request.method == 'PATCH':
        data = JSONParser().parse(request)

        # No need to process transaction if we don't have matches
        if len(data) < 1:
            return Response(status=status.HTTP_204_NO_CONTENT)

        Match.patch_list_of_matches(data['matches'], data['query_id'])
        return Response(status=status.HTTP_204_NO_CONTENT)
