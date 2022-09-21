from multiprocessing import context
from pipes import Template
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse

from main_app.forms import PostCreateForm
from .models import City, Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"


class Cities(TemplateView):
    template_name="cities/city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name= self.request.GET.get("name")
        if name != None:
            context["cities"]= City.objects.filter(name__icontains=name)
            context["header"]= f"Searching for {name}"
        else:
            context["cities"] = City.objects.all()
            context["header"]= "Trending Cities"
        return context

class CityCreate(CreateView):
    model= City
    fields=['name', 'img','country','body']
    template_name= "cities/city_create.html"

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})

class CityDetail(DetailView):
    model=City
    template_name="cities/city_detail.html"

class CityUpdate(UpdateView):
    model= City
    fields= ['name','img', 'country', 'body']
    template_name= "cities/city_update.html"
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})

class CityDelete(DeleteView):
    model= City
    template_name="cities/city_delete.html"
    success_url = "/cities/"



class Posts(TemplateView):
    template_name="posts/post_list.html"

    # ordring =[-id]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")

        if title != None:
            context["posts"] = Post.objects.filter(name_icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["posts"] = Post.objects.all()
            context["header"] = "posts"
        return context


# need to work on create not working

class PostCreate(CreateView):
    model = Post
    fields = ['name', 'image', 'author', 'body']
    template_name = "cities/city_create.html"

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})


class PostDtail(DetailView):
    model=Post
    template_name ="posts/post_detail.html"

    # def get_context_data(self, **kwargs):
    #     context= super(PostDtail, self).get_context_data(**kwargs)

    #     return context
    
