from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender=models.ForeignKey(User,related_name='sent_messages')
    receiver=models.ForeignKey(User,related_name='receiverd_messages')
    content=models.TextField(max_length = 500, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True) 
