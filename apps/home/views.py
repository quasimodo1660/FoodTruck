from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from ..users.models import Profile
from ..lunchbox.models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth import login
from django.db.models import Q

def index(request):
    user=request.user
    lunchboxImages = LunchboxImage.objects.all()
    return render(request,'home/home.html',{'user':user,'all_lunchboxes':Lunchbox.objects.all().order_by("-updated_at"),'LIS':lunchboxImages})



def search(request):
    t=request.POST['search']
    user_filter=User.objects.filter(Q(username__contains=t)|Q(first_name__contains=t)|Q(last_name__contains=t)|Q(email__contains=t)).filter(is_superuser=False).filter(~Q(username=request.user.username)).distinct()
    lunchbox_filter=Lunchbox.objects.filter(Q(title__contains=t)|Q(location__contains=t)|Q(tags__name__contains=t)|Q(user__username__contains=t)).filter(display=True).distinct()
    # print user_filter
    return render(request,'home/search.html',{'all_users':user_filter,'all_lunchboxes':lunchbox_filter,'user':request.user})