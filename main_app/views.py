from pipes import Template
from django.shortcuts import render 
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import City


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

class Cities(TemplateView):
    template_name="city_list.html"

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

class Post(TemplateView):
    template_name="post_list.html"
   