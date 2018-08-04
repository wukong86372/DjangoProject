from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Account,Message

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,'board/login.html',{'error':'jiushidengbushang'})
    else:
        messages = Message.objects.all()
        return render(request,'board/index.html',{'messages':messages})

def base(request):
    return render(request,'board/base.html')

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Account.objects.get(Q(username=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None
