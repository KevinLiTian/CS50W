""" Register all custom models in Django Admin """

from django.contrib import admin

from .models import User, Category, AuctionListing, Bid, Comment, WatchList

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionListing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(WatchList)
