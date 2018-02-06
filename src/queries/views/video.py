from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from queries.serializers import VideoSerializer
from queries.models import Video


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows videos to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
