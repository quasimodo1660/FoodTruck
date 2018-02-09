# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __unicode__(self):
       return self.name

class Tag(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,related_name='tags')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __unicode__(self):
       return self.name


class Lunchbox(models.Model):
    user = models.ForeignKey(User,related_name='lunchboxes')
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    description = models.TextField(max_length = 500, blank=True)
    city = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag,related_name='lunchboxes')
    offertime = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    public  = models.BooleanField(default = False)
    def __unicode__(self):
        return self.title


class Step(models.Model):
    lunchbox = models.ForeignKey(Lunchbox,related_name='steps')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    description = models.TextField(max_length = 500, blank=True)

def lunchbox_directory_path(Lunchbox,filename):
    print 'sbb'
    return 'Users/user_{0}/{1}/{2}'.format(Lunchbox.title,filename)

class LunchboxImage(models.Model):
    user= models.ForeignKey(User,related_name='lunchboxImages')
    lunchbox= models.ForeignKey(Lunchbox,related_name='images')
    image=models.ImageField(upload_to='media/test/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # def __unicode__(self):
    #     return self.image


# @receiver(post_save,sender=Lunchbox)
# def create_steps(sender,instance,created,**kwargs):
#     if created:
#         Step.objects.create(lunchbox=instance)

# @receiver(post_save,sender=Lunchbox)       
# def create_images(sender,instance,created,**kwargs):
#     if created:
#         LunchboxImage.objects.create(lunchbox=instance,user=instance.user)