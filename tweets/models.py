from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Tweet(models.Model):
    account = models.ForeignKey(to=User, on_delete=models.CASCADE)
    tweet = models.TextField()
    created_at = models.DateField(default=timezone.now)
