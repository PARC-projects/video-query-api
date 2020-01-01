from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.decorators import api_view

from queries.models import Profile
from queries.serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
