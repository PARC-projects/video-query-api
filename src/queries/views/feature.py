from rest_framework import viewsets

from queries.models import Feature
from queries.serializers import SignatureSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new feature instance.

    retrieve:
    Return the given feature.

    list:
    Return a list of all the existing features.

    update:
    Update a given feature as whole.

    partial_update:
    Update a set of parameters of a given feature.
    """
    queryset = Feature.objects.all()
    serializer_class = SignatureSerializer
