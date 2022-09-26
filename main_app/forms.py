from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import City, Post, Profile
from django.contrib.auth.models import User 

class PostCreateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'author', 'image','city', 'body')

    widgets ={
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'autor': forms.Select(attrs={'class':'form-control', 'palceholder':'user name'}),
        'image': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        'cityy': forms.TextInput(attrs={'class':'form-control'}),
    }


class SignUpForm(UserCreationForm):
        email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
        first_name =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
        last_name =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))

        class Meta:
            model =User
            fields=('username', 'first_name', 'last_name','email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'



class UpdateProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    username =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    avatar =forms.CharField(max_length=250, widget= forms.TextInput(attrs={'class':'form-control'}))
    # is_superuser =forms.CharField(max_length=100, widget= forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_staff =forms.CharField(max_length=100, widget= forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_active =forms.CharField(max_length=100, widget= forms.CheckboxInput(attrs={'class':'form-check'}))
    # date_joined =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        fields=('username', 'first_name', 'last_name','email', 'avatar')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 =forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 =forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class':'form-control','type':'password'}))

    class Meta:
        model =User
        fields=('old_password','new_password1', 'new_password2')
