""" Django Tests """
# pylint: disable=no-member, too-many-locals, unused-variable

from django.test import TestCase

from .models import User, Post, Follow, Like

# Create your tests here.
class NetworkTestCase(TestCase):
    """ Network App Test """

    def setUp(self):
        """ Setting up testing Database """

        # Create some users
        usr1 = User.objects.create_user(username="1")
        usr2 = User.objects.create_user(username="2")
        usr3 = User.objects.create_user(username="3")

        # Create some posts
        post1 = Post.objects.create(owner=usr1, content="Post 1")
        post2 = Post.objects.create(owner=usr2, content="Post 2")
        post3 = Post.objects.create(owner=usr3, content="Post 3")

        post4 = Post.objects.create(owner=usr1, content="Neg Like", likes=-1)

        # Create some follows
        follow1 = Follow.objects.create(user1=usr1, user2=usr2)
        follow2 = Follow.objects.create(user1=usr2, user2=usr3)
        follow3 = Follow.objects.create(user1=usr3, user2=usr1)

        follow4 = Follow.objects.create(user1=usr1, user2=usr1)

        # Create some likes
        like1 = Like.objects.create(usr=usr1, post=post1)
        like2 = Like.objects.create(usr=usr2, post=post3)
        like3 = Like.objects.create(usr=usr3, post=post3)

    def test_user_count(self):
        """ 3 Authenticated Users in total """
        self.assertEqual(User.objects.all().count(), 3)

    def test_post_count(self):
        """ 4 Posts in total """
        self.assertEqual(Post.objects.all().count(), 4)

    def test_follow_count(self):
        """ 4 Follows in total """
        self.assertEqual(Follow.objects.all().count(), 4)

    def test_like_count(self):
        """ 3 Likes in total """
        self.assertEqual(Like.objects.all().count(), 3)

    def test_usr1_post_count(self):
        """ Usr1 has 2 posts """
        usr1 = User.objects.get(username="1")
        self.assertEqual(usr1.posts.count(), 2)

    def test_valid_like(self):
        """ Valid Like Count """
        usr1 = User.objects.get(username="1")
        post1 = Post.objects.get(owner=usr1, content="Post 1")
        self.assertTrue(post1.valid_like())

    def test_invalid_like(self):
        """ Invalid Like Count """
        usr1 = User.objects.get(username="1")
        post4 = Post.objects.get(owner=usr1, content="Neg Like")
        self.assertFalse(post4.valid_like())

    def test_valid_follow(self):
        """ Valid Follow """
        usr1 = User.objects.get(username="1")
        usr2 = User.objects.get(username="2")
        follow1 = Follow.objects.get(user1=usr1, user2=usr2)
        self.assertTrue(follow1.valid_follow())

    def test_invalid_follow(self):
        """ Invalid Follow """
        usr1 = User.objects.get(username="1")
        follow4 = Follow.objects.get(user1=usr1, user2=usr1)
        self.assertFalse(follow4.valid_follow())
