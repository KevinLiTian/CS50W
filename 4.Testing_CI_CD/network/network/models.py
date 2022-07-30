""" Database """

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ All Users """

class Post(models.Model):
    """ All Posts """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}'s Post"

class Follow(models.Model):
    """ All User Followingsm (user1 follows user2) """
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_others')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='being_followed')

    def __str__(self):
        return f"{self.user1} is following {self.user2}"

class Like(models.Model):
    """ User Like Posts """
    usr = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liking')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
