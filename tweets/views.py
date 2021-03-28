from rest_framework import viewsets
from .serializers import TweetSerializer
from .models import Tweet
from rest_framework.response import Response
from rest_framework.decorators import api_view


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('created_at')
    serializer_class = TweetSerializer


@api_view(['GET'])
def list_tweets(Request):
    tweets_list = Tweet.objects.all().order_by('created_at')
    serializer = TweetSerializer(tweets_list, many=True)
    return Response(serializer.data)
