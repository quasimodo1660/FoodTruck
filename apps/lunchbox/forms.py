from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

class LunchboxForm(forms.ModelForm):
    class Meta:
        model=Lunchbox
        fields=('title','description','user')



