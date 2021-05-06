from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import UserProfile
# Create your views here.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
