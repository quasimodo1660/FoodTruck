from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth import login
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
import avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def update(request):
    print request.POST
    user=User.objects.get(pk=request.user.id)
    userProfile=Profile.objects.get(user_id=request.user.id)
    if request.POST['fn']!=user.first_name:
        user.first_name=request.POST['fn']
    if request.POST['ln']!=user.last_name:
        user.last_name=request.POST['ln']
    if request.POST['zip']!=userProfile.postal_code:
        userProfile.postal_code=request.POST['zip']
    if request.POST['phone']!=userProfile.phone:
        userProfile.phone=request.POST['phone']
    if request.POST['bio']!=userProfile.bio:
        userProfile.bio=request.POST['bio']
    try:
        user.save()
        userProfile.save()
        data={'success':'updated'}
    except:
        data={'errors':'Something wrong'}
    return JsonResponse(data)

def signup(request):
    print request
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            uf=user_form.save(commit=False)
            uf.set_password(uf.password)
            uf.save()
            # pf=profile_form.save(commit=False)
            # pf.user=uf
            # pf.save()
            login(request,uf)
            return redirect('/')
        else:
            if request.is_ajax(): 
                return JsonResponse({'success' : False, 'user_errors' : user_form.errors})
            else:
                messages.error(request, 'Please correct the error below.')
                return redirect('/accounts/signup')
            
    else:
        user_form = UserForm()
        # profile_form = ProfileForm()
    return render(request, 'user/regit.html', {
        'user_form': user_form,
        # 'profile_form': profile_form
    })


@login_required
def show(request,id):
    user=request.user
    puser=User.objects.get(pk=id)
    print user
    print puser
    return render(request,'user/user_info.html',{'user':user,'puser':puser})

def friendShip(request):
    # print 'needchangeB' in request.POST
    user=request.user
    tuser=User.objects.get(pk=request.POST['needchangeB'])
    puser=User.objects.get(pk=request.POST['puser'])
    if puser in user.profile.following.all():
        user.profile.following.remove(puser)       
        respone='follow'
    else:
        user.profile.following.add(puser)
        respone='unfollow'
    data=tuser.followers.count()
    data1=tuser.profile.following.count()
    return JsonResponse({'success':respone,'followers':data,'following':data1})
    
@login_required
def settingPofile(request,id):
    if request.method=='GET':
        user=User.objects.get(pk=id)
        PCform = PasswordChangeForm(user=request.user)
        return render(request,'user/profile.html',{'user':user,'PCform':PCform})
    if request.method=='POST':
        return HttpResponse('sbb')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer