# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *






@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','created_at','updated_at')
    



@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','name','created_at','updated_at','category_id')


@admin.register(Lunchbox)
class LunchboxAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('id','title','location','lon','lat')

@admin.register(LunchboxImage)
class LunchboxAdmin(admin.ModelAdmin):
    list_display=('user','lunchbox','image')

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('user','lunchbox','score','content','updated_at','created_at')