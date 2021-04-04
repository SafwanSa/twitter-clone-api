from rest_framework import viewsets
from .serializers import TweetSerializer
from .models import Tweet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.conf import settings

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('created_at')
    serializer_class = TweetSerializer


@api_view(['GET'])
def list_tweets(request):
    tweets_list = Tweet.objects.all().order_by('created_at')
    serializer = TweetSerializer(tweets_list, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_tweet(request):
    data = JSONParser().parse(request)
    serializer = TweetSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save(account=None)
        return Response(serializer.data)
    else:
        return Response(status=400)

@api_view(['GET'])
def get_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    serializer = TweetSerializer(tweet, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def like_post(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.liked_by.add(settings.AUTH_USER_MODEL)