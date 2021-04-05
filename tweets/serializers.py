from rest_framework import serializers
from .models import Tweet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class MyKeywordsField(serializers.RelatedField):
    def to_native(self, value):
        return {str(value.pk): value.name}


class TweetSerializer(serializers.ModelSerializer):
    account = UserSerializer(read_only=True)
    liked_by = UserSerializer(read_only=True, many=True)
    retweeted_by = UserSerializer(read_only=True, many=True)
    likes = serializers.IntegerField(source='get_likes')
    retweets = serializers.IntegerField(source='get_retweets')
    comments = MyKeywordsField(many=True, read_only=True)
    # parent = serializers.RelatedField()

    class Meta:
        model = Tweet
        fields = '__all__'
        read_only_fields = ['created_at']
