from django import forms
from django.contrib.auth.models import User
from .models import *
import zipcode
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, help_text='Required. Letters, digits and @/./+/-/_ only.')
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = User
        fields=('username','email','password')
    def clean_email(self):
        qs = User.objects.filter(email=self.cleaned_data['email'])
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.count():
            raise forms.ValidationError(
                'That email address is already in use')
        else:
            return self.cleaned_data['email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('postal_code',)
    def clean_postal_code(self) :
        value=self.cleaned_data['postal_code']
        if len(value)<5:
            raise ValidationError('Postal code must be 5 digits')
        if not ZIPCODE_REGEX.match(value):
            raise ValidationError('Postal code must be 5 digits')
        if not zipcode.isequal(str(value)):
            raise ValidationError('Invalid postal code')
        return self.cleaned_data['postal_code']
