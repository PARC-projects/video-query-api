from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from queries.serializers import QueryResultSerializer
from queries.models import QueryResult, Match

class QueryResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows query result to be viewed or edited.
    """
    queryset = QueryResult.objects.all()
    serializer_class = QueryResultSerializer

    @detail_route(methods=['get'])
    def matches(self, request, pk):
        """
        Get videos based on dataset id
        """
        return Response(Match.objects.filter(query_result_id=pk).values())
