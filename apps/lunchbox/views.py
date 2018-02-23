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
    return render(request,'lunchbox/create.html')


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


class LunchboxViewSet(viewsets.ModelViewSet):
    queryset = Lunchbox.objects.all().order_by('-updated_at')
    serializer_class = LunchboxSerializer
    # @datail_route(methods=['GET'])
    # def image(self, request, *args, **kwargs):
    #     pass