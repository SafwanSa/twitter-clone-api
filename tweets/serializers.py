from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TweetSerializer(serializers.ModelSerializer):
    account = UserSerializer()

    class Meta:
        model = Tweet
        fields = ['account', 'tweet', 'created_at']
