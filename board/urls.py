from django.urls import path,include

from . import  views,auth_views

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('register/',auth_views.register, name='register'),
    path('like/', views.like, name='like'),
]


