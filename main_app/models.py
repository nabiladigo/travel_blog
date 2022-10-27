
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class City(models.Model):
    name= models.CharField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="image/")
    country= models.CharField(max_length=250)
    body= models.TextField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_cites')


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_detail', args=(str(self.id)))

    


class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="image/")
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body=RichTextField(blank=True, nul=True)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    city= models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities")
    
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    
    class Meta:
        ordering =["-post_date"]
        

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True )
    bio = models.TextField()
    email = models.CharField(max_length=100, null=True )
    avatar = models.ImageField(default='profile_images', upload_to='profile_images')
    city = models.CharField(max_length=100)

    website_url = models.CharField(max_length=225, null=True, blank=True )
    facebook_url = models.CharField(max_length=225, null=True, blank=True )
    instagram_url = models.CharField(max_length=225, null=True, blank=True )
    twitter_url = models.CharField(max_length=225, null=True, blank=True )

    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse('home')


