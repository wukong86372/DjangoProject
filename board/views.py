from django.shortcuts import render

from . import models
# Create your views here.
def index(request):
    messages = models.Message.objects.all()
    return render(request,'board/index.html',{'messages':messages})

def base(request):
    return render(request,'board/base.html')
