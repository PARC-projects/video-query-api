from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from queries.models import SearchSet, Feature
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
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    @action(methods=['get'], detail=True)
    def videos(self, request, pk):
        """
        GET videos based on search set id
        """
        return Response(SearchSet.get_videos_based_on_search_set_id(pk))

    @action(methods=['get'], detail=True)
    def features(self, request, pk):
        """
        GET features based on search set id
        """
        return Response(Feature.objects.filter(video_clip__video__searchset__in=pk).values())
