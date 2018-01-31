# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from .models import *


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