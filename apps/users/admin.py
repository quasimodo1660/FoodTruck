from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
@admin.register(UserAvater)
class UserAvaterAdmin(admin.ModelAdmin):
    list_display = ('user','image')