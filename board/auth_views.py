from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username and password:
            username = username.strip()
            try:
                user = auth.authenticate(request, username=username, password=password)
                if user:
                    auth.login(request,user)
                    return redirect('board:index')
                else:
                    error = '用户名或密码错误!'
            except:
                error = '用户名或密码错误!'
                return render(request, 'board/login.html', {'error': error})
    return render(request, 'board/login.html',{'error': error})


def logout(request):
    auth.logout(request)
    return redirect('board:index')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2', None)
        error = '成功创建！'
        if password1 != password2:
            error = '两次密码不一致！'
        else:
            user = User.objects.filter(username=username)
            if user:
                error = '用户名已存在!'
            else:
                user = User()
                user.username = username
                user.set_password(password1)
                user.save()
        return render(request, 'board/register.html', {'error': error})
    return render(request, 'board/register.html')
