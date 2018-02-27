# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render,HttpResponse
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.http import JsonResponse
import time
from .serializers import *
from rest_framework import viewsets


# Create your views here.
def index(request):
   pass


def add(request):
    return render(request,'lunchbox/add.html')

def update(request):
    print request.user
    print request.POST
    print request.FILES
    return HttpResponse('sbb')

def uplaods(request):
    if request.method =='POST':
        photo = LunchboxImage.objects.create(user=request.user,lunchbox = Lunchbox.objects.last(),image=request.FILES['file'])
        if photo:
            data = {'is_valid': True, 'name': photo.image.name, 'url': photo.image.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

# complie by Frank
def next(request):
    if request.method =='POST':
        print request.POST
        print request.POST['title']
        print request.user
        Lunchbox.objects.create(user=request.user,title = request.POST['title'],description = request.POST['des'])
        category = Category.objects.all().name      
        return render(request,'lunchbox/add.html')
# end of Frank's code

class LunchboxViewSet(viewsets.ModelViewSet):
    queryset = Lunchbox.objects.all().order_by('-updated_at')
    serializer_class = LunchboxSerializer
    # @datail_route(methods=['GET'])
    # def image(self, request, *args, **kwargs):
    #     pass

def show(request,id):
    lunchbox=Lunchbox.objects.get(pk=int(id))
    user=request.user
    return render(request,'lunchbox/showOne.html',{lunchbox:lunchbox,user:user})

def showAn(request,id):
    return render(request,'Client/dist/index.html')