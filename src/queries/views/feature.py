from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from queries.models import Feature
from queries.serializers import FeatureSerializer


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
    serializer_class = FeatureSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('video_clip', 'dnn_stream__name',)
    filter_fields = ('video_clip', 'dnn_stream', 'dnn_stream_split',)
