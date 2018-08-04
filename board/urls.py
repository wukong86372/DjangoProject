from django.urls import path,include

from . import  views,auth_views

urlpatterns = [

    path('index/', views.index, name='index'),
    #url(r'^login/$', views.login, name='login'),
    path('login/', auth_views.login, name='login'),
    # url(r'^authenticate/$', auth_views.authenticate, name='authenticate'),
    path('logout/', auth_views.logout, name='logout'),
    path('register/',auth_views.register, name='register'),
    path('',views.base, name='base'),
]


