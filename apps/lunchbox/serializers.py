from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class LunchboxSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=LunchboxImage.objects.all())
    class Meta:
        model=Lunchbox
        fields = ('user','title','description','lon','lat','offertime','images')