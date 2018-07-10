from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from avatar.models import Avatar
from avatar.utils import (
    cache_result,
    get_default_avatar_url,
    get_user_model,
    get_user,
)
from avatar.views import _get_avatars

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    following = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ('user','bio','birth_date','postal_code','phone','following')
        read_only_fields = ('url',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)
    # avatar = serializers.PrimaryKeyRelatedField(many=False, queryset=Avatar.objects.get(''))
    avatar = serializers.SerializerMethodField('render_avatar')
    followers = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id','url', 'username', 'avatar','email','followers','profile')
    def render_avatar(self, obj):
        print obj.socialaccount_set.first()
        # user = User.objects.get(pk=obj.id)
        if obj.socialaccount_set.first():
            return obj.socialaccount_set.first().get_avatar_url()
        else:
           return ''
        # return obj.id


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

