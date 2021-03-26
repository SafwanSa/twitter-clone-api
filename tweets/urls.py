from django.urls import path, include
from .views import TweetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tweets', TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
