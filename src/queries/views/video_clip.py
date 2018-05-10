from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from queries.models import VideoClip
from queries.serializers import VideoClipSerializer


class VideoClipViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new video clip instance.

    retrieve:
    Return the given video clip.

    list:
    Return a list of all the existing video clips.

    update:
    Update a given video clip as whole.

    partial_update:
    Update a set of parameters of a video clip.
    """
    queryset = VideoClip.objects.all()
    serializer_class = VideoClipSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('video__name', 'clip')
