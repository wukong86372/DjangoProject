
from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser
# Create your models here.

class Account(AbstractBaseUser):
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=512)
    last_login = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username



class Message(models.Model):
    username = models.CharField(max_length=512)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1024)
    data_added = models.DateTimeField(auto_now_add=True)
    like_num = models.IntegerField()
    dislike_num = models.IntegerField()

    def __str__(self):
        return self.title
