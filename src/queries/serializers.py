from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SearchSetSerializer(serializers.ModelSerializer):
    videos = None

    class Meta:
        model = SearchSet
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    search_sets = SearchSetSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


SearchSetSerializer.videos = VideoSerializer(many=True, read_only=True)


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            'id', 'query_result', 'score', 'user_match', 'query_id', 'reference_video_id', 'reference_time', 'is_match')


class QueryResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryResult
        fields = '__all__'


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class VideoClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoClip
        fields = '__all__'
