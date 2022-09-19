from django.db import models

# Create your models here.


class City(models.Model):
    name= models.CharField(max_length=100, unique=True)
    img= models.CharField(max_length=250)
    country= models.CharField(max_length=250)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name