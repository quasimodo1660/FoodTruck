from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import zipcode
import re
from datetime import datetime

PHONE_REGEX = re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{4}')
ZIPCODE_REGEX =re.compile(r'^\d{5}$')
present=datetime.now()

# Customize validator
# def validateZipcode(value):
#     if len(value)<5:
#         raise ValidationError(
#            '{} must be longer than: 5'.format(value) 
#         )
#     if not ZIPCODE_REGEX.match(value):
#         raise ValidationError(
#            '{} must be 5 digits'.format(value) 
#         )
#     if not zipcode.isequal(str(value)):
#         raise ValidationError(
#            'Invalid Zip code'
#         )
        





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    postal_code= models.CharField(max_length=10, blank=False)
    phone = models.CharField(max_length=15, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
        

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()