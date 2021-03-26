from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.HyperlinkedModelSerializer):
  model = Tweet
  fields = '__all__'