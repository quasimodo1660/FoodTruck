from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
from avatar.models import Avatar





class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(many=False, queryset=Profile.objects.all())
    # avatar = serializers.PrimaryKeyRelatedField(many=False, queryset=Avatar.objects.get(''))
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'groups','profile')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Profile
        fields = ('bio','birth_date','postal_code','phone')