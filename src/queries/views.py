from rest_framework import viewsets
from .serializers import *
from .models import *


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

class QueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows video queries to be viewed or edited.
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer


class MatchArrayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows matched arrays to be viewed or edited.
    """
    queryset = MatchArray.objects.all()
    serializer_class = MatchArraySerializer


class SignatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows signatures to be viewed or edited.
    """
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
