from django.contrib.auth.models import User
from rest_framework import viewsets

from queries.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing users.

    retrieve:
    Return the given user.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
