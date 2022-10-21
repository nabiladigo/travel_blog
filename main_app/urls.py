from django.urls import path 
from . import views
from .views import profile, postlike
# , citylike 

urlpatterns =[
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('cities/', views.Cities.as_view(), name="city_list"),
    path('cities/new', views.CityCreate.as_view(), name="city_create"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name="city_detail"),
    path('cities/<int:pk>/update', views.CityUpdate.as_view(), name="city_update"),
    path('cities/<int:pk>/delete', views.CityDelete.as_view(), name="city_delete"),
    
    
    path('cities/posts/new', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('like/<int:pk>/', postlike, name="post_like"),

    path('accounts/signup', views.Signup.as_view(), name="signup"),
    path('profile/', profile, name="profile"),
    path('profile_update/', views.ProfileUpdate.as_view(), name="profile_update"),
   
    path('password/', views.PasswordChange.as_view(template_name="registration/change_password.html")),
    path('password_success', views.password_success, name="password_success"),

]