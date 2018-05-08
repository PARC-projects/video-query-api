from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from queries.serializers import SearchSetSerializer
from queries.models import SearchSet


class SearchSetViewSet(viewsets.ModelViewSet):
    """
    create:
    Create a new search set instance.

    retrieve:
    Return the given search set.

    list:
    Return a list of all the existing search sets.

    update:
    Update a given search set as whole.

    partial_update:
    Update a set of parameters of a search set.
    """
    queryset = SearchSet.objects.all()
    serializer_class = SearchSetSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    @detail_route(methods=['get'])
    def videos(self, request, pk):
        """
        GET videos based on search set id
        """
        return Response(SearchSet.get_videos_based_on_search_set_id(pk))
