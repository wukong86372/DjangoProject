from django.shortcuts import render

from . import models
# Create your views here.
def login(request):
    print("haha")
    return render(request,'users/login.html')