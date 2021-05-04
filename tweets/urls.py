from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views

# router = routers.DefaultRouter()
# router.register('tweets', TweetViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('tweets/', list_tweets),
    path('tweets-create/', create_tweet),
    path('tweets/<pk>', get_tweet),
    path('tweets-like/<pk>', toggle_like),
    path('tweets-retweet/<pk>', toggle_retweet),
    path('tweets-delete/<pk>', delete_tweet),
    path('tweets-comment/<pk>', comment),
    path('auth-token/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('silk/', include('silk.urls', namespace='silk'))
]
