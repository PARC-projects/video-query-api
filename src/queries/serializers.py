from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

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
        fields = (
            'id', 'name', 'search_set_to_query', 'video', 'reference_time', 'max_matches_for_review',
            'notes', 'reference_clip_image', 'process_state', 'last_modified', 'reference_clip_number',
            'reference_clip_pk', 'clip_duration', 'use_dynamic_target_adjustment', 'final_report_file',
            'final_report_url', 'video_name', 'dataset'
        )


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            'id', 'query_result', 'score', 'user_match', 'video_clip', 'query_id', 'reference_video_id',
            'reference_time', 'reference_video_external_source', 'match_video_path', 'match_video_time_span', 'is_match',
            'match_video_name', 'reference_start_time', 'reference_end_time'
        )


class QueryResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryResult
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'


class VideoClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoClip
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
