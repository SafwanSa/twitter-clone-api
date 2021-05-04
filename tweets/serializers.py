from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CommentSerializer(serializers.RelatedField):
    def to_native(self, value):
        return {str(value.pk): value.id}

    def to_representation(self, data):
        serializer = TweetSerializer(data)
        return serializer.data


class TweetSerializer(serializers.ModelSerializer):
    account = UserSerializer(read_only=True)
    # liked_by = UserSerializer(read_only=True, many=True)
    # retweeted_by = UserSerializer(read_only=True, many=True)
    # likes = serializers.IntegerField(source='get_likes', read_only=True)
    # retweets = serializers.IntegerField(source='get_retweets', read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tweet
        fields = ['tweet', 'created_at', 'account']
        read_only_fields = ['created_at']
        # exclude = ['parent']
