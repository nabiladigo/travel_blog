from dataclasses import fields
from django import forms
from .models import City, Post, Profile

class PostCreateForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'author', 'image', 'body')

    widgets ={
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'autor': forms.TextInput(attrs={'class':'form-control'}),
        'image': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.TextInput(attrs={'class':'form-control'}),
    }


class UpdateProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    username =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    profile_pic =forms.CharField(max_length=250, widget= forms.TextInput(attrs={'class':'form-control'}))
    is_superuser =forms.CharField(max_length=100, widget= forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff =forms.CharField(max_length=100, widget= forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active =forms.CharField(max_length=100, widget= forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined =forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        fields=('username', 'first_name', 'last_name','email', 'password', 'profile_pic')
