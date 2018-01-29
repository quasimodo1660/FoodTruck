# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __unicode__(self):
       return self.name

class Tag(models.Model):
    name=models.CharField(max_length=255)
    category_id=models.ForeignKey(Category,related_name='tags')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __unicode__(self):
       return self.name


class Lunchbox(models.Model):
    user = models.ForeignKey(User,related_name='lunchboxes')
    title = models.CharField(max_length=255)
    lon = models.FloatField()
    lat = models.FloatField()
    description = models.TextField(max_length = 500, blank=True)
    city = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag,related_name='lunchboxes')
    offertime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    public  = models.BooleanField(default = False)


class Step(models.Model):
    lunchbox = models.ForeignKey(Lunchbox,related_name='steps')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    description = models.TextField(max_length = 500, blank=True)

def lunchbox_directory_path(User,Lunchbox,filename):
    return 'Users/user_{0}/{1}/{2}'.format(User.id,Lunchbox.title,filename)

class LunchboxImage(models.Model):
    user=user = models.ForeignKey(User,related_name='lunchboxImages')
    lunchbox= models.ForeignKey(Lunchbox,related_name='images')
    image=models.ImageField(upload_to=lunchbox_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)