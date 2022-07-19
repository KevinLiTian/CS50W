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
        "auc_list": AuctionListing.objects.filter(active=True)
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

def listing(request, listing_id):
    """ Listing Pages """
    user = request.user
    item = AuctionListing.objects.get(id=listing_id)
    comment = Comment.objects.filter(auc_list=listing_id)
    price = item.price
    minbid = price

    # Check for bids on the item
    if Bid.objects.filter(auc_list=listing_id).exists():
        bid_obj = Bid.objects.order_by('-amount').first()
        item.price = bid_obj.amount
        item.save()
        minbid = float(price) + 0.01

    # Check if user is waching this list
    watching = False
    if user.is_authenticated:
        watch_list = user.watch.all()
        auc_list = [watch.auc_list for watch in watch_list]
        if item in auc_list:
            watching = True

    return render(request, "auctions/listing.html", {
        "id": item.id,
        "owner": item.user,
        "title": item.name,
        "description": item.description,
        "category": item.category,
        "price": price,
        "minbid": minbid,
        "imgurl": item.imgurl,
        "comments": comment,
        "watching": watching
    })

@login_required(login_url="login")
def bid(request):
    """ User Bid on an Item """
    listing_id = request.POST['listing_id']
    bidamount = request.POST['bidamount']
    item = AuctionListing.objects.get(id=listing_id)
    item.price = bidamount
    item.save()

    if Bid.objects.filter(user=request.user, auc_list=listing_id).exists():
        bid_in_db = Bid.objects.get(user=request.user, auc_list=listing_id)
        bid_in_db.amount = bidamount
        bid_in_db.save()
        return redirect("listing", listing_id)

    Bid.objects.create(
        user=request.user, auc_list=item, amount=bidamount)

    return redirect("listing", listing_id)

@login_required(login_url="login")
def comments(request):
    """ User Comment on an Item """
    listing_id = request.POST['listing_id']
    commenting = request.POST['commenting']
    item = AuctionListing.objects.get(id=listing_id)
    Comment.objects.create(user=request.user, comment=commenting, auc_list=item)
    return redirect("listing", listing_id)

@login_required(login_url="login")
def watch(request):
    """ Watch List """
    user = request.user
    watch_list = user.watch.all()
    auc_list = [watch.auc_list for watch in watch_list]
    return render(request, "auctions/watch.html", {
        "user": user,
        "auc_list": auc_list
    })

@login_required(login_url="login")
def delwatch(request, listing_id):
    """ Delete from Watch List """
    pass

@login_required(login_url="login")
def addwatch(request, listing_id):
    """ Add to Watch List """
    pass
