from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from ..users.serializers import *


class LunchboxSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    images = serializers.StringRelatedField(many=True)
    tags = serializers.StringRelatedField(many=True)
    reviews = serializers.StringRelatedField(many=True)
    class Meta:
        model=Lunchbox
        fields = ('url','user','title','description','lon','lat','offertime','images','tags','reviews','like')
        read_only_fields = ('url','images')