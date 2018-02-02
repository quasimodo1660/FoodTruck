# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
import time

# Create your views here.
def index(request):
    return render(request,'lunchbox/create.html')


def add(request):
    lunchbox = Lunchbox.objects.get(id=55)
    return render(request,'lunchbox/add.html',{'lunchbox':lunchbox})

def update(request):
    print request.user
    print request.POST
    print request.FILES
    return HttpResponse('sbb')

def uplaods(request):
    # print('recieve request')
    # print request.FILES
    # photo = LunchboxImage.objects.create(user=request.user,lunchbox = Lunchbox.objects.get(id=55),image=request.FILES)
    # if photo:
    #     data = {'is_valid': True, 'name': photo.image.name, 'url': photo.image.url}
    # else:
    #     data = {'is_valid': False}
    # return JsonResponse(data)
    form = LunchboxImageForm(request.POST, request.FILES)
    form.user = request.user
    form.lunchbox = Lunchbox.objects.get(id=55)
    print 'valid'
    if form.is_valid():
        photo = form.save()
        data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
    else:
        data = {'is_valid': False}
    return JsonResponse(data)