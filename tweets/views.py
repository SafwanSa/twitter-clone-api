from rest_framework import viewsets
from .serializers import TweetSerializer
from .models import Tweet
# Create your views here.

class TweetViewSet(viewsets.ModelViewSet):
  queryset = Tweet.objects.all().order_by('created_at')
  serializer = TweetSerializer


