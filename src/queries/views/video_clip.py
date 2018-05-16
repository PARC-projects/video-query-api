from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from queries.models import VideoClip, Feature
from queries.serializers import VideoClipSerializer


class VideoClipViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new video clip instance.<br/>
    (video, clip, duration) set must be unique.

    retrieve:
    Return the given video clip.

    list:
    Return a list of all the existing video clips. <br/>
    Search term:  video name, clip number

    update:
    Update a given video clip as whole.

    partial_update:
    Update a set of parameters of a video clip.

    """
    queryset = VideoClip.objects.all()
    serializer_class = VideoClipSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('video__name', '=clip', '=duration')
    filter_fields = ('video__name', 'clip', 'duration')

    @action(methods=['get'], detail=True)
    def features(self, request, pk):
        """
        GET features based on video clip id
        """
        return Response(Feature.objects.filter(video_clip_id=pk).values())
