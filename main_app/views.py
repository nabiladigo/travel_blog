import re
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# from main_app.forms import PostCreateForm
from .models import City, Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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


@method_decorator(login_required, name='dispatch')
class CityCreate(CreateView):
    model= City
    fields=['name', 'img','country','body']
    template_name= "cities/city_create.html"

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})



class CityDetail(DetailView):
    model=City
    template_name="cities/city_detail.html"


@method_decorator(login_required, name='dispatch')
class CityUpdate(UpdateView):
    model= City
    fields= ['name','img', 'country', 'body']
    template_name= "cities/city_update.html"
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    fields = ['name', 'image', 'author', 'body']
    template_name = "cities/city_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('post_detail', kwargs={'pk': self.object.pk})




class PostDtail(DetailView):
    model=Post
    template_name ="posts/post_detail.html"

    # def get_context_data(self, **kwargs):
    #     context= super(PostDtail, self).get_context_data(**kwargs)

    #     return context
    

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ['image', 'title', 'author', 'body']
    template_name = "posts/post_update.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = "/posts/"





class Signup(View):
    def get(self, request):
        form= UserCreationForm()
        context ={"form": form }
        return render( request, "registration/signup.html", context)

    def post(self, request):
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect("post_list")

        else:
            context= {"form": form}
            return render(request, "registration/signup.html", context)
