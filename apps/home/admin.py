from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Message)
class MsgAdmin(admin.ModelAdmin):
    list_display = ('id','sender','receiver','content','created_at')
