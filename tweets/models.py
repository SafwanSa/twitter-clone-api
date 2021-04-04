from django.db import models
# from django.utils import timezone
import datetime
from django.contrib.auth.models import User
# Create your models here.


class Tweet(models.Model):
    account = models.ForeignKey(
        to=User, on_delete=models.CASCADE, blank=True, null=True)
    tweet = models.TextField()
    created_at = models.DateField(default=datetime.date.today)
