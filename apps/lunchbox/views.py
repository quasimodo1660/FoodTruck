# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render,HttpResponse,redirect
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
from datetime import datetime
from django.utils import timezone
from avatar.models import Avatar
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def index(request):
   pass

@login_required
def add(request):
    category = Category.objects.all()
    tag1 = Tag.objects.filter(category=Category.objects.get(id=1))
    tag2 = Tag.objects.filter(category=Category.objects.get(id=2))
    tag3 = Tag.objects.filter(category=Category.objects.get(id=3))
    tag4 = Tag.objects.filter(category=Category.objects.get(id=4))
    tag5 = Tag.objects.filter(category=Category.objects.get(id=5))
    tag6 = Tag.objects.filter(category=Category.objects.get(id=6))
    tag7 = Tag.objects.filter(category=Category.objects.get(id=7))
    tag8 = Tag.objects.filter(category=Category.objects.get(id=8))
    
    return render(request,'lunchbox/add.html',{'category':category,'tag1':tag1,
    'tag2':tag2,'tag3':tag3,'tag4':tag4,'tag5':tag5,'tag6':tag6,'tag7':tag7,'tag8':tag8,})

@login_required
def update(request,id):
    bento=Lunchbox.objects.get(pk=id)
    if request.method=='DELETE':
        bento.display=False
        try:
            bento.save()
            data={'success':'hide a bento'}
        except:
            data={'errors':'Something wrong'}
        return JsonResponse(data)
    if request.method=='GET':
        category = Category.objects.all()
        tag1 = Tag.objects.filter(category=Category.objects.get(id=1))
        tag2 = Tag.objects.filter(category=Category.objects.get(id=2))
        tag3 = Tag.objects.filter(category=Category.objects.get(id=3))
        tag4 = Tag.objects.filter(category=Category.objects.get(id=4))
        tag5 = Tag.objects.filter(category=Category.objects.get(id=5))
        tag6 = Tag.objects.filter(category=Category.objects.get(id=6))
        tag7 = Tag.objects.filter(category=Category.objects.get(id=7))
        tag8 = Tag.objects.filter(category=Category.objects.get(id=8))
        return render(request,'lunchbox/edit.html',{'bento':bento,'category':category,'tag1':tag1,
    'tag2':tag2,'tag3':tag3,'tag4':tag4,'tag5':tag5,'tag6':tag6,'tag7':tag7,'tag8':tag8})
    if request.method=='POST':
        offertime1=request.POST['time']
        bento.title=request.POST['title']
        bento.description = request.POST['des']
        bento.location = request.POST['loc']
        bento.offertime = offertime1
        bento.lon = request.POST['lng']
        bento.lat= request.POST['lat']
        try:
            bento.save()
            data={'success':'updated','update_at':bento.update_at}
        except:
            data={'errors':'Something wrong'}
        return JsonResponse(data)

def uplaods(request):
    if request.method =='POST':
        print request.POST['lunchBoxID2']
        photo = LunchboxImage.objects.create(user=request.user,lunchbox = Lunchbox.objects.get(pk=request.POST['lunchBoxID2']),image=request.FILES['file'])
        if photo:
            data = {'is_valid': True, 'name': photo.image.name, 'url': photo.image.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


# complie by Frank
def next(request):
    offerTime1=datetime.strptime(request.POST['time'],'%d %B, %Y').strftime('%Y-%m-%d')
    lunchbox=Lunchbox.objects.create(user=request.user,title = request.POST['title'],description = request.POST['des'],location = request.POST['loc'],offertime = offerTime1,lon = request.POST['lng'],lat= request.POST['lat'])
    if lunchbox:
        data={'lID':lunchbox.id}
    else:
        data={'errors':'Something wrong'}
    return JsonResponse(data)

def tag(request):
    if request.method =='POST':
        print request.POST['lunchboxID']
        for x in request.POST.getlist('foo'):
            this_tag = Tag.objects.get(id=x)
            this_lunchbox = Lunchbox.objects.get(id = request.POST['lunchboxID'])
            this_lunchbox.tags.add(this_tag)
        return redirect('/')
# end of Frank's code


@xframe_options_exempt
def show(request,id):
    lunchbox=Lunchbox.objects.get(pk=int(id))
    user=request.user
    return render(request,'lunchbox/showOne.html',{'lunchbox':lunchbox,'user':user})

def showAn(request,id):   
    request.session = request.user.id
    return render(request,'Client/dist/index.html')

def getUser(request):
    data={
        'username':request.user.username,
        'uID':request.user.id,
    }
    return JsonResponse(data)


def createReview(request):
    if request.method=='POST':
        lunchbox=lunchbox=Lunchbox.objects.get(pk=request.POST['bentoID'])
        review=Review.objects.create(user=request.user,lunchbox=lunchbox,score=request.POST['score'],content=request.POST['content'])
        return render(request,'lunchbox/review.html',{'lunchbox':lunchbox})      
        

def addLike(request,id):
    if request.method=='POST':
        lunchbox=Lunchbox.objects.get(pk=id)
        # print lunchbox.like
        if request.user in lunchbox.likedby.all():
            lunchbox.like-=1
            lunchbox.likedby.remove(request.user)
            data={'succes':'remove like',
            'userid':request.user.id}
        else:
            lunchbox.like+=1
            lunchbox.likedby.add(request.user)
            data={'succes':'add like',
            'userid':request.user.id,
            'username':request.user.username}
        lunchbox.save()
        # print lunchbox.like
        # print request.POST
        return JsonResponse(data)       
        
# REVIEW STUFF
def deleteReview(request,id):
    if request.method=='DELETE':
        try:
            Review.objects.get(pk=id).delete()
            count=User.objects.get(pk=request.user.id).reviews.count()
            data={'success':'review deleted','count':count}
        except:
            data={'errors':'Something wrong'}
        return JsonResponse(data)
    if request.method=='POST':
        review=Review.objects.get(pk=id)
        review.score=request.POST['stars']
        review.content=request.POST['content']
        try:
            review.save()
            data={'success':'review edited','stars':review.score,'content':review.content}
        except:
            data={'errors':'Something wrong'}
        return JsonResponse(data)
        
# Moblie stuff
@csrf_exempt
def moblieUpload(request):
    if request.method=='POST':
        # print request.POST
        user=User.objects.get(pk=request.POST['user'])
        tags = json.loads(request.POST['tags'])
        try:
            lunchbox=Lunchbox.objects.create(user=user,title = request.POST['title'],description = request.POST['des'],location = request.POST['loc'],offertime = request.POST['offertime'],lon = request.POST['lng'],lat= request.POST['lat'])
            LunchboxImage.objects.create(user=user,lunchbox = lunchbox,image=request.FILES['photo'])
            for x in tags:
                # print x
                this_tag = Tag.objects.get(id=int(x['id']))
                lunchbox.tags.add(this_tag)
            data={'success':'add a bento'}
        except:
            data={'errors':'Something wrong'}
        # print tags[0].id
        # print request.body  
        # print request.FILES
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


class LunchboxImageViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = LunchboxImage.objects.all().order_by('lunchbox')
    serializer_class = LunchboxImageSerializer
      
    # @detail_route(methods=['post'])
    # @method_decorator(csrf_exempt)
    # def createReview(self,request):
    #     print 'here'

class AvatarImageViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Avatar.objects.all().order_by('user')
    serializer_class = AvatarImageSerializer


class CategoryViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer