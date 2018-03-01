# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-27 18:36
from __future__ import unicode_literals

import apps.lunchbox.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchbox', '0006_auto_20180209_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunchbox',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lunchboximage',
            name='image',
            field=models.ImageField(upload_to=apps.lunchbox.models.lunchbox_directory_path),
        ),
    ]