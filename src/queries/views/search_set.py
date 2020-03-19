from django.http import JsonResponse
from rest_framework import viewsets, filters
from rest_framework.decorators import action, api_view
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
    filter_backends = (DjangoFilterBackend, SearchFilter,
                       filters.OrderingFilter)
    search_fields = ('name',)
    filter_fields = ('name',)
    ordering_fields = ('name', 'date_created',)

    @action(methods=['get'], detail=True)
    def videos(self, request, pk):
        """
        GET videos based on search set id
        """
        videos = Video.objects.filter(searchset__id=pk)

        searchTerm = self.request.query_params.get('searchTerm', None)
        if searchTerm is not None:
            videos = videos.filter(name__icontains=searchTerm)

        ordering = self.request.query_params.get('ordering', None)
        if ordering is not None:
            videos = videos.order_by(ordering)

        return Response(videos.values())

    @action(methods=['get'], detail=True)
    def features(self, request, pk):
        """
        GET features based on search set id
        """
        duration = SearchSet.objects.get(pk=pk).duration
        return Response(Feature.objects.filter(video_clip__video__searchset=pk,
                                               video_clip__duration=duration).values())

    @action(methods=['get'], detail=True)
    def all(self, request):
        """
        GET all search sets i.e. bypass pagination
        """
        return Response(SearchSet.objects.all().values())


@api_view(['GET'])
def search_sets_all(request):
    results = SearchSetSerializer(SearchSet.objects.all(), many=True).data
    return JsonResponse({
        "results": results
    })
