from django.urls import path 
from . import views

urlpatterns =[
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cities/', views.Cities.as_view(), name="city_list"),
    path('posts/', views.Post.as_view(), name="post_list"),
]