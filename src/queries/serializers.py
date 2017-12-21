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


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
    # dataset = DatasetSerializer(many=False, read_only=True)
    # video = VideoSerializer(many=False, read_only=True)

    class Meta:
        model = Query
        fields = '__all__'


class MatchedArraySerializer(serializers.ModelSerializer):
    query = QuerySerializer(many=False, read_only=True)

    class Meta:
        model = MatchedArray
        fields = '__all__'


class SignatureSerializer(serializers.ModelSerializer):
    video = VideoSerializer(many=False, read_only=True)

    class Meta:
        model = Signature
        fields = '__all__'
