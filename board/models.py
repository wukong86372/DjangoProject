
from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=512)
    password = models.CharField(max_length=512)
    data_last = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Message(models.Model):
    username = models.CharField(max_length=512)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1024)
    data_added = models.DateTimeField(auto_now_add=True)
    likeNum = models.IntegerField()
    dislikeNum = models.IntegerField()

    def __str__(self):
        return self.title
