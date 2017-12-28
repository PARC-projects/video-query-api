from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows videos to be viewed or edited.
    """
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows datasets to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    @detail_route(methods=['get'])
    def videos(self, request, pk):
        """
        Get videos based on dataset id
        """
        return JsonResponse(Video.objects.filter(dataset_id=pk).values())


class QueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows queries to be viewed or edited.
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    @detail_route(methods=['get'])
    def query_result(self, request, pk):
        """
        Get latest query result based on query id
        """
        return Response(QueryResultSerializer(Query.get_latestest_query_result_by_query_id(self, pk), many=False).data)

    @detail_route(methods=['get'])
    def matches(self, request, pk):
        """
        Get latest matches based on query id
        """
        return Response(MatchSerializer(Query.get_latestest_matches_by_query_id(self, pk), many=True).data)


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


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows match to be viewed or edited.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class SignatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows signatures to be viewed or edited.
    """
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
