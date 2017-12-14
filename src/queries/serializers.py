from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'name', 'dataset_id')


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'name')


class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('__all__')


class MatchedArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchedArray
        fields = ('__all__')


class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = ('__all__')
