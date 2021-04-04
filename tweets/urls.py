from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tweets-list', list_tweets),
    path('tweets-create', create_tweet),
    path('tweets/<pk>', get_tweet),
    path('tweets-like/<pk>', like_post),
    path('auth-token', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
