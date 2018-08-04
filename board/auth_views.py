from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.forms import models
from django.shortcuts import render, redirect
from .models import Account

def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        error = '用户名和密码均不能为空！'
        if username and password:
            username = username.strip()
            try:
                user = Account.objects.get(username=username)
                ps_hash = make_password(password)
                ps_bool = check_password(password,ps_hash)
                if ps_bool:
                    return redirect('board:index')
                else:
                    error = '用户名或密码错误!'
            except:
                error = '密码错误！'
            return render(request, 'board/login.html', {'error': error})
    return render(request, 'board/login.html')

def logout(request):
    auth.logout(request)
    return redirect('board:logout')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2', None)
        error = '成功创建！'
        if password1 != password2:
            error = '两次密码不一致！'
        else:
            user = Account.objects.filter(username=username)
            if user:
                error = '用户名已存在!'
            else:
                password = make_password(password1)
                user = Account.objects.create(username=username, password=password)
                user.save()
        return render(request, 'board/register.html', {'error': error})
    return render(request, 'board/register.html')
