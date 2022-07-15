""" Register all custom models in Django Admin """

from django.contrib import admin

from .models import User

# Register your models here.
admin.site.register(User)
