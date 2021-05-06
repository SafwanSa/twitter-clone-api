from django.db import models

# Create your models here.


class UserProfile(models.Model):
    e = models.CharField(max_length=200)
