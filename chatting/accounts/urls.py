__author__ = 'judelee'
from django.conf.urls import patterns, url

from django.conf.urls import url
from accounts import views as account_view

urlpatterns = [
    url(r'^login/(\w*)', account_view.login_page, name='login'),
]