from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Account,Message

# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #     return render(request,'board/login.html',{'error':'jiushidengbushang'})
    # else:
    messages = Message.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        message = Message()
        message.text = text
        message.username = request.user.username;
        message.title = title
        message.dislike_num = 0;
        message.like_num = 0
        message.save()
        return redirect('board:index')
    return render(request,'board/index.html',{'messages':messages})

def base(request):
    return render(request,'board/base.html')


