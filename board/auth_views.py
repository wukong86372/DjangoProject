from django.contrib import auth
from django.contrib.auth.hashers import make_password
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
            return render(request, 'board/login.html', {'error': '用户名或密码错误!'})
    else:
        return render(request, 'board/login.html', {'error': ''})

def logout(request):
    auth.logout(request)
    return redirect('board:logout')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2', None)
        if password1 != password2:
            return render(request, 'board/register.html', {'error': '两次密码不一致！'})
        user = auth.authenticate(username=username)
        if len(user) > 0:
            return render(request, 'board/register.html', {'error': '用户名已存在!'})
        else:
            password = make_password(password1)
            user = User.objects.create(username=username, password=password)
            user.save()
            return render(request, 'board/register.html', {'error': '成功创建'})

    return render(request, 'board/register.html')
