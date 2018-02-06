from rest_framework import viewsets
from queries.serializers import SignatureSerializer
from queries.models import Signature


class SignatureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows signatures to be viewed or edited.
    """
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
