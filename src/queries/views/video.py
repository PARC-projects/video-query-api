from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from queries.models import Video
from queries.serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new video instance.

    retrieve:
    Return the given video.

    list:
    Return a list of all the existing videos.<br/>
    Search term: video name and/or video path

    update:
    Update a given video as whole.

    partial_update:
    Update a set of parameters of a video.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'path')
    filter_fields = ('name', 'path')
