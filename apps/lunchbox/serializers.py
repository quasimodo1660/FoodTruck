from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from ..users.serializers import *
from avatar.models import Avatar

class LunchboxImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=LunchboxImage
        fields=('image',)

class AvatarImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Avatar
        fields=('url','avatar')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    user_avatar1 = serializers.ReadOnlyField(source='user.avatar_url()')
    user_avatar = AvatarImageSerializer(many=True,read_only=True)
    user_name = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model=Review
        fields=('user','user_name','user_avatar1','user_avatar','user_id','lunchbox','score','content','updated_at','created_at')
        read_only_fields = ('url','user_avatar1')


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

