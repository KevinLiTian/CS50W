""" Django Tests """
# pylint: disable=no-member, too-many-locals, unused-variable

from django.test import TestCase
from django.contrib.auth.models import AnonymousUser

from .models import User, Post, Follow, Like

# Create your tests here.
class NetworkTestCase(TestCase):
    """ Network App Test """

    def setup(self):
        """ Setting up testing Database """

        # Create some users
        usr1 = User.objects.create_user(username="1")
        usr2 = User.objects.create_user(username="2")
        usr3 = User.objects.create_user(username="3")

        anonymous_usr = AnonymousUser(username="anonymous")

        # Create some posts
        post1 = Post.objects.create(owner=usr1, content="Post 1")
        post2 = Post.objects.create(owner=usr2, content="Post 2")
        post3 = Post.objects.create(owner=usr3, content="Post 3")

        post4 = Post.objects.create(owner=anonymous_usr, content="Anonymous")
        post5 = Post.objects.create(owner=usr1, content="Neg Like", likes=-1)

        # Create some follows
        follow1 = Follow.objects.create(user1=usr1, user2=usr2)
        follow2 = Follow.objects.create(user1=usr2, user2=usr3)
        follow3 = Follow.objects.create(user1=usr3, user2=usr1)

        follow4 = Follow.objects.create(user1=anonymous_usr, user2=usr1)
        follow5 = Follow.objects.create(user1=usr1, user2=usr1)
        follow6 = Follow.objects.create(user1=anonymous_usr, user2=anonymous_usr)

        # Create some likes
        like1 = Like.objects.create(usr=usr1, post=post1)
        like2 = Like.objects.create(usr=usr2, post=post2)
        like3 = Like.objects.create(usr=usr3, post=post3)

        like4 = Like.objects.create(usr=anonymous_usr, post=post1)
