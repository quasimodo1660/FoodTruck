from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from ..users.models import Profile
from ..lunchbox.models import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth import login
from django.db.models import Q

from .models import *



def home(request):
    print request.user_agent.is_mobile
    if request.user_agent.is_mobile and request.user.is_authenticated:
        response = HttpResponse('',status=302)
        response['Location']='BENTOMAN://login?user=124'
        return redirect('')
        return response['Location'] 
    else:
        return render(request,'home/index.html',{'user':request.user})



def index(request):
    if request.user_agent.is_mobile:
        response=HttpResponse("",status=302)
        response['Location']="bentoman://id="+str(request.user.id)
        return response
    else:
        user=request.user
        lunchboxImages = LunchboxImage.objects.all()
        return render(request,'home/home.html',{'user':user,'all_lunchboxes':Lunchbox.objects.all().order_by("-updated_at"),'LIS':lunchboxImages})



def search(request):
    t=request.POST['search']
    user_filter=User.objects.filter(Q(username__contains=t)|Q(first_name__contains=t)|Q(last_name__contains=t)|Q(email__contains=t)).filter(is_superuser=False).filter(~Q(username=request.user.username)).distinct()
    lunchbox_filter=Lunchbox.objects.filter(Q(title__contains=t)|Q(location__contains=t)|Q(tags__name__contains=t)|Q(user__username__contains=t)).filter(display=True).distinct()
    # print user_filter
    return render(request,'home/search.html',{'all_users':user_filter,'all_lunchboxes':lunchbox_filter,'user':request.user})


def chat_users(request):
    # print request.POST
    if 'purpose' in request.POST:
        chater=User.objects.get(pk=request.POST['rid'])
        Message.objects.create(sender=request.user,receiver=chater,content=request.POST['msg_type_content'])
        return JsonResponse({'success':'add a message'})
    else:
        chater=User.objects.get(pk=request.POST['uid'])
    # return JsonResponse({'sbb':'ajj'})   
        msg_list=Message.objects.filter(Q(sender=request.user,receiver=chater)|Q(receiver=request.user,sender=chater)).order_by('created_at')
    # print msg_list
        return render(request,'home/msg_list.html',{'cid':request.POST['cid'],'chater':chater,'user':request.user,'msg_list':msg_list})


def chat(request):
    print request.user
    return render(request,'chat.html',{'user':request.user})