""" Django Models (Database) """

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ User Table """
    nickname = models.CharField(max_length=64, unique=True, default="None")

    def __str__(self):
        return f"{self.nickname}"

class Category(models.Model):
    """ Category Table
    Category
    """
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class AuctionListing(models.Model):
    """ Auction Listing Table
    User_posted  name  price  Category  description  imgURL  active
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postings")
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,
                            on_delete=models.CASCADE,
                            related_name="category_listing")
    imgurl = models.URLField(max_length=255, blank=True,
                    default="https://ualr.edu/elearning/files/2020/10/No-Photo-Available.jpg")

    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} posted by {self.user}. Current price is ${self.price}"

class Bid(models.Model):
    """ Bids Table
    User  AuctionListing  bid_amount
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bid")
    auc_list = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bid amount of {self.amount} by {self.user} for {self.auc_list}"

class Comment(models.Model):
    """ Comments Table
    User  comment  Auctionlisting
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    auc_list = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return f"\"{self.comment}\" by {self.user} on {self.auc_list}"

class WatchList(models.Model):
    """ Watch List Table
    User  AuctionListing
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watch")
    auc_list = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.auc_list} watched by {self.user}"
