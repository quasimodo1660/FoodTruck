# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunchbox', '0009_lunchbox_ingredient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lunchbox',
            options={'ordering': ['updated_at']},
        ),
        migrations.AlterField(
            model_name='lunchbox',
            name='city',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
