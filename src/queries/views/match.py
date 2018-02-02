from rest_framework import viewsets
from queries.serializers import MatchSerializer
from queries.models import Match


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows match to be viewed or edited.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
