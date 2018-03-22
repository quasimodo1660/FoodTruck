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



def update(request):
    print request.POST
    user=User.objects.get(pk=request.user.id)
    if request.POST['fn']!=user.first_name:
        user.first_name=request.POST['fn']
    if request.POST['ln']!=user.last_name:
        user.last_name=request.POST['ln']
    if request.POST['zip']!=user.profile.postal_code:
        user.profile.postal_code=request.POST['zip']
    if request.POST['phone']!=user.profile.phone:
        user.profile.phone=request.POST['phone']
    if request.POST['bio']!=user.profile.bio:
        user.profile.bio=request.POST['bio']
    user.save()
    if user:
        data={'success':'updated'}
    else:
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

def show(request,id):
    user=request.user
    return render(request,'user/user_info.html',{user:user})



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