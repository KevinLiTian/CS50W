""" Views """
# pylint: disable=no-member

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import User, Post, Follow


def index(request):
    """ Index View """

    # POST
    if request.method == "POST":
        owner = User.objects.get(id=request.user.id)
        content = request.POST['content']
        Post.objects.create(owner=owner, content=content)
        return redirect('index')

    # GET
    posts = Post.objects.order_by("-timestamp")

    paginator = Paginator(posts, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "posts": page_obj
    })


def login_view(request):
    """ Login View """

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("index")

        return render(request, "network/login.html", {
            "message": "Invalid username and/or password."
        })

    return render(request, "network/login.html")


def logout_view(request):
    """ Logout View """

    logout(request)
    return redirect("index")


def register(request):
    """ Register View """

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect("index")

    return render(request, "network/register.html")


def profile(request, username):
    """ User Profile """
    if request.method == "POST":
        pass

    usr = User.objects.get(username=username)


    is_following = (Follow.objects.filter(user1=request.user, user2=usr)
                    if request.user.is_authenticated
                    else None)

    posts = usr.posts.all()
    paginator = Paginator(posts, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        "owner": username,
        "posts": page_obj,
        "following": usr.following_others.count(),
        "follower": usr.being_followed.count(),
        "is_following": is_following
    })


@login_required(login_url="login")
def follow(request, username):
    """ Follow Other User """

    usr = User.objects.get(username=username)
    if request.user != usr:
        Follow.objects.create(user1=request.user, user2=usr)

    return redirect('profile', username)


@login_required(login_url="login")
def unfollow(request, username):
    """ Unfollow a User """

    usr = User.objects.get(username=username)
    follow_obj = Follow.objects.filter(user1=request.user, user2=usr)

    if follow_obj:
        follow_obj.delete()

    return redirect('profile', username)


@login_required(login_url="login")
def following(request):
    """ Show Posts by Followings """

    usr = User.objects.get(username=request.user)
    followed_users = [followed.user2 for followed in usr.following_others.all()]
    posts = Post.objects.filter(owner__in=followed_users)

    paginator = Paginator(posts, 10) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'network/following.html', {
        "posts": page_obj
    })
