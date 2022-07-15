""" Django Models (Database) """

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ User Table """
    nickname = models.CharField(max_length=64, default="None")
