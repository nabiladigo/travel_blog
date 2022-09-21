from dataclasses import fields
from django import forms
from .models import City, Post

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
