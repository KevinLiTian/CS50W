""" Database """

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ All Users """

class Post(models.Model):
    """ All Posts """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    likes = models.IntegerField()

class Follow(models.Model):
    """ All User Followingsm (user1 follows user2) """
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_others')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)
