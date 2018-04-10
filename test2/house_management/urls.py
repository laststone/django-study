from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^user(\d+)', views.userinfo),
    url(r'^user(\d+)', views.userhouse),
    url(r'house(\d+)', views.userhouse),
    url(r'order(\d+)', views.userorder)
]