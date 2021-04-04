from django.urls import path, include
from .views import TweetViewSet, list_tweets, create_tweet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tweets-list', list_tweets),
    path('tweets-create', create_tweet),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
