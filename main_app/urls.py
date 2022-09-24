from django.urls import path 
from . import views

urlpatterns =[
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cities/', views.Cities.as_view(), name="city_list"),
    path('cities/new', views.CityCreate.as_view(), name="city_create"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('cities/<int:pk>/update', views.CityUpdate.as_view(), name="city_update"),
    path('cities/<int:pk>/delete', views.CityDelete.as_view(), name="city_delete"),

    path('posts', views.Posts.as_view(), name="post_list"),
    path('cities/posts/new', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/', views.PostDtail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),

    path('accounts/signup', views.Signup.as_view(), name="signup"),
    path('profile/<int:pk>', views.ProfilePage.as_view(), name= "profile"),
    path('profile_update/<int:pk>', views.ProfileUpdate.as_view(), name="profile_update")
]