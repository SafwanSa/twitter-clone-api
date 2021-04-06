from rest_framework import viewsets
from .serializers import TweetSerializer
from .models import Tweet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from copy import deepcopy


# class TweetViewSet(viewsets.ModelViewSet):
#     queryset = Tweet.objects.all().order_by('created_at')
#     serializer_class = TweetSerializer


@api_view(['GET'])
def list_tweets(request):
    tweets_list = Tweet.objects.all().order_by('created_at')
    serializer = TweetSerializer(tweets_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_tweet(request):
    data = JSONParser().parse(request)
    serializer = TweetSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save(account=request.user)
        return Response(serializer.data)
    else:
        return Response(status=400)


@api_view(['GET'])
def get_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    serializer = TweetSerializer(tweet, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    deleted = deepcopy(tweet)
    tweet.delete()
    serializer = TweetSerializer(deleted)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def toggle_like(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    liked_by = tweet.liked_by.all()
    if request.user in liked_by:
        tweet.liked_by.remove(request.user.id)
    else:
        tweet.liked_by.add(request.user.id)
    serializer = TweetSerializer(tweet)
    return Response(serializer.data)


@ api_view(['POST'])
@ permission_classes((IsAuthenticated, ))
def toggle_retweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    retweeted_by = tweet.retweeted_by.all()
    if request.user in retweeted_by:
        tweet.retweeted_by.remove(request.user.id)
    else:
        tweet.retweeted_by.add(request.user.id)
    serializer = TweetSerializer(tweet)
    return Response(serializer.data)


@ api_view(['POST'])
def comment(request, pk):
    data = JSONParser().parse(request)
    data['parent'] = pk
    serializer = TweetSerializer(data=data, many=False)
    serializer.is_valid(raise_exception=True)
    if serializer.is_valid():
        serializer.save(account=request.user.id)
        return Response(serializer.data)
    else:
        return Response(status=400)
