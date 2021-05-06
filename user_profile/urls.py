from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls))
]
