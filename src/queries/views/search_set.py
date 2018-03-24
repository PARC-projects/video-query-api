from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from queries.serializers import SearchSetSerializer
from queries.models import SearchSet


class SearchSetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.
    <br/>
    <br/>
    <b>search-set/{id}/videos</b>
    <ul>
        <li>GET: Get videos based on search set id.</li>
    </ul>
    """
    queryset = SearchSet.objects.all()
    serializer_class = SearchSetSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    @detail_route(methods=['get'])
    def videos(self, request, pk):
        """
        Get videos based on search set id
        """
        return Response(SearchSet.get_videos_based_on_search_set_id(pk))
