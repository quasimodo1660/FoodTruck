from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from ..users.serializers import *

class LunchboxImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=LunchboxImage
        fields=('image',)

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    user_avatar = serializers.ReadOnlyField(source='user.Avatar.avatar')
    user_name = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model=Review
        fields=('user','user_name','user_avatar','user_id','lunchbox','score','content','updated_at','created_at')


class LunchboxSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    # user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    images = LunchboxImageSerializer(many=True,read_only=True)
    tags = serializers.StringRelatedField(many=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    ingredient = serializers.StringRelatedField(many=True)
    class Meta:
        model=Lunchbox
        fields = ('url','user','user_id','title','description','lon','lat','offertime','images','tags','reviews','like','ingredient')
        read_only_fields = ('url','images')

