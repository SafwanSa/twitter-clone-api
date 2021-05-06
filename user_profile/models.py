from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    account = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    avatar = models.CharField(max_length=200)
