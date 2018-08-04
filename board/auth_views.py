from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            messages = models.Message.objects.all()
            return render(request, 'board/index.html', {'messages': messages})
        else:
            return render(request, 'board/login.html', {'error': 'username or password error!'})
    else:
        return render(request, 'board/login.html', {'error': ''})

def logout(request):
    auth.logout(request)
    return redirect('board:logout')

