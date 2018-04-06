from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from ..users.models import Profile
from ..lunchbox.models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth import login

def index(request):
    user=request.user
    lunchboxImages = LunchboxImage.objects.all()
    return render(request,'home/home.html',{'user':user,'all_lunchboxes':Lunchbox.objects.all().order_by("-updated_at"),'LIS':lunchboxImages})



def search(request):
    return HttpResponse('sbb')