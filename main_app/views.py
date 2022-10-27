from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect


from .models import City, Post, Profile ,User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.views import generic

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import PostCreateForm, ProfilePageForm, UpdateProfileForm, SignUpForm, PasswordChangingForm
from django.urls import reverse, reverse_lazy


# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"


# city views

class Cities(TemplateView):
    template_name="cities/city_list.html"
    ordring = ['-id']

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
    fields=['name', 'image','country','body']
    template_name= "cities/city_create.html"

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.pk})


class CityDetail(DetailView):
    model=City
    template_name="cities/city_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super(CityDetail, self).get_context_data(**kwargs)

    #     stuff = get_object_or_404(City, id=self.kwargs['pk'])
    #     total_likes = stuff.total_likes()

    #     liked = False
    #     if stuff.likes.filter(id=self.request.user.id).exists():
    #         liked = True

    #     context["total_likes"] = total_likes
    #     context["liked"] = liked

    #     return context


# def citylike(request, pk):
#     city = get_object_or_404(City, id=request.POST.get('city_id'))
#     liked = False
#     if city.likes.filter(id=request.user.id).exists():
#         city.likes.remove(request.user)
#         liked = False
#     else:
#         city.likes.add(request.user)
#         liked = True

    # to stay in the same page without the user notice anything
    # return HttpResponseRedirect(reverse('city_detail', args=[str(pk)]))


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


# Post views

# need to work on create not working

@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "posts/post_create.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(PostCreate, self).form_valid(form)


class PostDetail(DetailView):
    model=Post
    template_name ="posts/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked

        return context


def postlike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    # to stay in the same page without the user notice anything
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


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


# User views

class Signup(generic.CreateView):
    form_class= SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('profile')


class ProfilePage(DetailView):
    model= Profile
    template_name= "registration/profile_page.html"

    def get_context_data(self,*args, **kwargs):
        users=Profile.objects.all()
        context = super(ProfilePage, self).get_context_data(*args,**kwargs) 

        page_user=get_object_or_404(Profile, id=self.kwargs['pk'])      
        context["page_user"] = page_user
        return context


class CreateProfilePage(CreateView):
    model=Profile
    form_class= ProfilePageForm
    template_name= "registration/create_profile_page.html"
    # fields= '__all__'

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)

        
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         profile_form= UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if  profile_form.is_valid():

#             profile.save()
#             messages.success(request, 'Your profile is updated successfully')

#             return redirect(to = 'registration/profile.html')
#     else:

#         profile_form= UpdateProfileForm(instance=request.user.profile)  
        
#         return render(request, 'registration/profile.html',  {'profile_form': profile_form})
   

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = UpdateProfileForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('profile')

    # success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})
