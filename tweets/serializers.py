from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class TweetSerializer(serializers.ModelSerializer):
    account = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'account', 'tweet', 'created_at']
        read_only_fields = ['created_at']
