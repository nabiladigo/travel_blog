import email
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class City(models.Model):
    name= models.CharField(max_length=100, unique=True)
    img= models.CharField(max_length=250)
    country= models.CharField(max_length=250)
    body= models.TextField(max_length=500)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.CharField(max_length=250)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    city= models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities")
    # this to associate post to a user to filter our post by user logged in
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="first name")
    last_name = models.CharField(max_length=100, default="last name")
    username = models.CharField(max_length=100, default="last name")
    email = models.CharField(max_length=100, default="last name")
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    city = models.CharField(max_length=60)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


