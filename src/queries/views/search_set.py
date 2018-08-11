from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from queries.models import SearchSet, Feature, Video
from queries.serializers import SearchSetSerializer


class SearchSetViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new search set instance.

    retrieve:
    Return the given search set.

    list:
    Return a list of all the existing search sets. <br/>
    Search term: search set name

    update:
    Update a given search set as whole.

    partial_update:
    Update a set of parameters of a search set.
    """
    queryset = SearchSet.objects.all()
    serializer_class = SearchSetSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filter_fields = ('name',)

    @action(methods=['get'], detail=True)
    def videos(self, request, pk):
        """
        GET videos based on search set id
        """

        if 'searchTerm' in request.query_params:
            return Response(
                Video.objects
                .filter(searchset__id=pk)
                .filter(name__icontains=request.query_params['searchTerm']).values()
            )
        else:
            return Response(Video.objects.filter(searchset__id=pk).values())

    @action(methods=['get'], detail=True)
    def features(self, request, pk):
        """
        GET features based on search set id
        """
        duration = SearchSet.objects.get(pk=pk).duration
        return Response(Feature.objects.filter(video_clip__video__searchset=pk,
                        video_clip__duration=duration).values())
