from rest_framework import viewsets
from queries.serializers import SignatureSerializer
from queries.models import Feature


class FeatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows signatures to be viewed or edited.
    """
    queryset = Feature.objects.all()
    serializer_class = SignatureSerializer
