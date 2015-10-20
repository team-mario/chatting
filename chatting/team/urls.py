__author__ = 'judelee'
from django.conf.urls import url
from team import views

urlpatterns = [
    url(r'^login/(\w*)', views.login_page, name='login'),
    url(r'^main/', views.main_page, name='main'),
]
