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
from django.views.decorators.csrf import csrf_exempt 
from rest_framework import mixins
from rest_framework.decorators import detail_route, list_route
from django.utils.decorators import method_decorator
import json


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



def show(request,id):
    lunchbox=Lunchbox.objects.get(pk=int(id))
    user=request.user
    return render(request,'lunchbox/showOne.html',{lunchbox:lunchbox,user:user})

def showAn(request,id):
    request.session = request.user.id
    return render(request,'Client/dist/index.html')

def getUser(request):
    data={
        'username':request.user.username,
        'uID':request.user.id,
    }
    return JsonResponse(data)

@csrf_exempt
def createReview(request):
    if request.method=='POST':
        temp = json.loads(request.body)
        review=Review.objects.create(user=request.user,lunchbox=Lunchbox.objects.get(pk=temp['lunchbox']),score=temp['score'],content=temp['content'])
        if review:
            data={'succes':'Add a review'}
        else:
            data={'errors':'Something wrong'}
        return JsonResponse(data)       
        





# API view
class LunchboxViewSet(viewsets.ModelViewSet):
    queryset = Lunchbox.objects.all().order_by('-updated_at')
    serializer_class = LunchboxSerializer
    # @datail_route(methods=['GET'])
    # def image(self, request, *args, **kwargs):
    #     pass

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('lunchbox')
    serializer_class = ReviewSerializer

@csrf_exempt
class LunchboxImageViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = LunchboxImage.objects.all().order_by('lunchbox')
    serializer_class = LunchboxImageSerializer
      
    # @detail_route(methods=['post'])
    # @method_decorator(csrf_exempt)
    # def createReview(self,request):
    #     print 'here'