""" View Functions """
# pylint: disable=no-member

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import NewListingForm


def index(request):
    """ Index View """
    return render(request, "auctions/index.html", {
        "auc_list": AuctionListing.objects.all()
    })


def login_view(request):
    """ Login View
    If POST request, then log user in if information matches database
    If GET request, render the login page
    """
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("index")

        return render(request, "auctions/login.html", {
            "message": "Invalid username and/or password."
        })

    # GET
    return render(request, "auctions/login.html")


def logout_view(request):
    """ Logout View """
    logout(request)
    return redirect("index")


def register(request):
    """ Register View
    If POST request, try to register a new user
    If GET request, render the registration form
    """
    if request.method == "POST":
        username = request.POST["username"]
        nickname = request.POST["nickname"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, nickname=nickname)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect("index")

    # GET
    return render(request, "auctions/register.html")

@login_required(login_url="login")
def new(request):
    """ Create new listing """
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            category = Category.objects.get(id=request.POST["category"])
            imgurl = form.cleaned_data["url"]

            AuctionListing.objects.create(user=user, name=title, description=description,
                price=price, category=category, imgurl=imgurl)

            return redirect("index")

    return render(request, "auctions/new.html", {
        "form": NewListingForm(),
        "categories": Category.objects.all()
    })
