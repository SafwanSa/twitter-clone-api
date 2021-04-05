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
    liked_by = models.ManyToManyField(to=User, related_name='liked_by')
    retweeted_by = models.ManyToManyField(to=User, related_name="retweeted_by")

    def __str__(self):
        return self.tweet

    def get_likes(self):
        return self.liked_by.count()

    def get_retweets(self):
        return self.retweeted_by.count()
