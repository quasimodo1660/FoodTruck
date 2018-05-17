# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-08 21:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20180326_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='chating',
            field=models.ManyToManyField(blank=True, related_name='related_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
