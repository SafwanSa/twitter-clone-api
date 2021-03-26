from django.db import models
# Create your models here.

class Tweet(models.Model):
  tweet = models.TextField()
  created_at = models.DateField()