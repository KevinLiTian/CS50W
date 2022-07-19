""" Relevant URLs """

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("listing/<str:listing_id>", views.listing, name="listing"),
    path("bid", views.bid, name="bid"),
    path("comment", views.comments, name="comment"),
    path("watch", views.watch, name="watch"),
    path("delwatch/<str:listing_id>", views.delwatch, name="delwatch"),
    path("addwatch/<str:listing_id>", views.addwatch, name="addwatch"),
    path("close/<str:listing_id>", views.close, name="close")
]
