from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'rink', 'gender', 'color', 'part', 'tag')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'rink', 'gender', 'color', 'part', 'tag')
