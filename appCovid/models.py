from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Costumer(models.Model):

    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    publish = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)
    profil = models.ImageField(upload_to='image_render', blank=True,
                               null=True, height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# class Costumer(models.Model):
#     """
#     docstring
#     """
#     user = models.OneToOneField(User, Null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=50)
#     phone = models.CharField(max_length=30)
