from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5, blank=True)


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="images", null=True)
    professional_profile = models.CharField(max_length=100)


class Portafolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.PROTECT)
