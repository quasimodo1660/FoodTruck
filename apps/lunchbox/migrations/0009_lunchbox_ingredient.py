# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchbox', '0008_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunchbox',
            name='ingredient',
            field=models.ManyToManyField(related_name='lunchboxes_ingredient', to='lunchbox.Tag'),
        ),
    ]
