from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()

class Hobby(models.Model):
    Party = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=100)

    def __str__(self):
        return (self.Party)