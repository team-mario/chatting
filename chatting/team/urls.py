__author__ = 'judelee'
from django.conf.urls import patterns, url
from team import views

urlpatterns = [
    url(r'^login/(\w*)', views.login_page, name='login'),
]
