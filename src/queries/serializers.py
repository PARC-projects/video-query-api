from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Video, VideoDataset, Query, MatchArray, Signature


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('__all__')


class VideoDatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoDataset
        fields = ('__all__')


class QuerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Query
        fields = ('__all__')


class MatchArraySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MatchArray
        fields = ('__all__')


class SignatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signature
        fields = ('__all__')
