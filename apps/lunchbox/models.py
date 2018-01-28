# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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