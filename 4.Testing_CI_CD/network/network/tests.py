""" Django Tests """
# pylint: disable=no-member, too-many-locals, unused-variable

import json
from django.test import TestCase, Client

from .models import User, Post, Follow, Like


# Global Response Code
SUCCESS_CODE = 200
REDIRECT_CODE = 302
BAD_REQUEST_CODE = 400
NA_CODE = 404


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


    # Database Testing
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


    # Client Testing
    def test_index(self):
        """ Test Index Page """
        client = Client()

        # Get Index Page
        response = client.get("")
        self.assertEqual(response.status_code, SUCCESS_CODE)
        self.assertEqual(len(response.context["posts"]), 4)

        # Post new Post (with new test user)
        test_user = User.objects.create(username='testuser')
        test_user.set_password('12345')
        test_user.save()

        login = client.login(username='testuser', password='12345')
        self.assertTrue(login)

        response = client.post("", {"content": "Example Post"})
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_login(self):
        """ Test Login Page """
        client = Client()

        # Get Login Page
        response = client.get("/login")
        self.assertEqual(response.status_code, SUCCESS_CODE)

        # Login POST request (with new test user)
        test_user = User.objects.create(username='testuser')
        test_user.set_password("12345")
        test_user.save()

        login = client.login(username="testuser", password="12345")
        self.assertTrue(login)

    def test_logout(self):
        """ Test Logout page """
        client = Client()

        response = client.get("/logout")
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_register(self):
        """ Test Register Page """
        client = Client()

        # Get Register Page
        response = client.get("/register")
        self.assertEqual(response.status_code, SUCCESS_CODE)

        # Register POST Register
        response = client.post("/register", {
            "username": "testuser",
            "email": "test@gmail.com",
            "password": "12345",
            "confirmation": "12345"
        })
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_profile(self):
        """ Test Profile Page """
        client = Client()

        # Correct Profile Username
        response = client.get("/profile/1")
        self.assertEqual(response.status_code, SUCCESS_CODE)

        # Incorrect Username
        response = client.get("/profile/foo")
        self.assertEqual(response.status_code, NA_CODE)

    def test_follow(self):
        """ Test Follow Action """
        client = Client()

        # Not Logged In
        response = client.get("/follow/<str:username>")
        self.assertEqual(response.status_code, REDIRECT_CODE)

        # Login but Follow not existed user
        test_user = User.objects.create(username='testuser')
        test_user.set_password("12345")
        test_user.save()

        login = client.login(username="testuser", password="12345")
        self.assertTrue(login)

        response = client.get("/follow/foo")
        self.assertEqual(response.status_code, NA_CODE)

        # Login and Follow existed user
        response = client.get("/follow/1")
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_unfollow(self):
        """ Test Unfollow Action """
        client = Client()

        # Not Logged In
        response = client.get("/unfollow/<str:username>")
        self.assertEqual(response.status_code, REDIRECT_CODE)

        # Login but Unfollow not existed user
        test_user = User.objects.create(username='testuser')
        test_user.set_password("12345")
        test_user.save()

        login = client.login(username="testuser", password="12345")
        self.assertTrue(login)

        response = client.get("/unfollow/foo")
        self.assertEqual(response.status_code, NA_CODE)

        # Login and Unfollow existed user
        response = client.get("/follow/1")
        self.assertEqual(response.status_code, REDIRECT_CODE)

        response = client.get("/unfollow/1")
        self.assertEqual(response.status_code, REDIRECT_CODE)

    def test_following(self):
        """ Test Following Page """
        client = Client()

        # Not logged in
        response = client.get("/following")
        self.assertEqual(response.status_code, REDIRECT_CODE)

        # Logged in
        test_user = User.objects.create(username='testuser')
        test_user.set_password("12345")
        test_user.save()

        login = client.login(username="testuser", password="12345")
        self.assertTrue(login)

        response = client.get("/following")
        self.assertEqual(response.status_code, SUCCESS_CODE)

    def test_edit(self):
        """ Test Edit API """
        client = Client()

        # Not logged in
        response = client.get("/edit/<str:post_id>")
        self.assertEqual(response.status_code, REDIRECT_CODE)

        # Logged in but edit none existing post
        test_user = User.objects.create(username='testuser')
        test_user.set_password("12345")
        test_user.save()

        login = client.login(username="testuser", password="12345")
        self.assertTrue(login)

        response = client.get("/edit/1000")
        self.assertEqual(response.status_code, NA_CODE)

        # Logged in, edit correct post but wrong request methods
        response = client.get("/edit/1")
        self.assertEqual(response.status_code, BAD_REQUEST_CODE)
        response = client.post("/edit/2")
        self.assertEqual(response.status_code, BAD_REQUEST_CODE)

        # Logged in, edit correct post, correct method but no content
        response = client.put("/edit/3", json.dumps({
            "No Content": "No content"
        }))
        self.assertEqual(response.status_code, BAD_REQUEST_CODE)

        # All correct
        response = client.put("/edit/3", json.dumps({
            "content": "Example content"
        }))
        self.assertEqual(response.status_code, SUCCESS_CODE)

    def test_like(self):
        """ Test Like API """
        client = Client()

        # Not logged in
        response = client.get("/like/<str:post_id>")
        self.assertEqual(response.status_code, REDIRECT_CODE)

        # Logged in but like none existing post
        test_user = User.objects.create(username='testuser')
        test_user.set_password("12345")
        test_user.save()

        login = client.login(username="testuser", password="12345")
        self.assertTrue(login)

        response = client.get("/like/1000")
        self.assertEqual(response.status_code, NA_CODE)

        # Logged in, like correct post but wrong request methods
        response = client.get("/like/1")
        self.assertEqual(response.status_code, BAD_REQUEST_CODE)
        response = client.post("/like/2")
        self.assertEqual(response.status_code, BAD_REQUEST_CODE)

        # Logged in, like correct post, correct method but no content
        response = client.put("/like/3", json.dumps({
            "No Content": "No content"
        }))
        self.assertEqual(response.status_code, BAD_REQUEST_CODE)

        # All correct
        response = client.put("/like/3", json.dumps({
            "like": "true"
        }))
        self.assertEqual(response.status_code, SUCCESS_CODE)
