from django.conf.urls import url,include
from django.contrib.auth.views import login_required
from . import  views

urlpatterns = [
    url(r'^login/$', login_required(),{'template_name': 'users/login.html'}, name='login'),
]


