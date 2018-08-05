from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
# Create your models here.
class Message(models.Model):
    username = models.CharField(max_length=512)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1024)
    data_added = models.DateTimeField(auto_now_add=True)
    like_num = models.IntegerField()
    dislike_num = models.IntegerField()

    def __str__(self):
        return self.title

class Like(models.Model):
    message_id = models.IntegerField()
    person_id = models.IntegerField()
    like_date = models.DateTimeField(auto_now_add=True)
    like_type = models.BooleanField(default=True)
