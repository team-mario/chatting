"""chatting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

urlpatterns = [
    url(r'^messages/project-plan$', 'message.views.message_list'),
    url(r'^messages/create$', 'message.views.message_create'),
    url(r'^messages/receive$', 'message.views.message_receive'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}),
    url(r'^register/success/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', 'login.views.register_page'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'post_change_redirect': 'message.views.message_list'}),
    url(r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done'),
    url(r'^accounts/profile/', 'team.views.index'),
    url(r'^issue/create$', 'team.views.channel_create', name='channel_create'),
    url(r'^create/room', 'team.views.create_room'),
    url(r'^room/detail/(?P<room_name>\S+)', 'team.views.room_detail'),
    url(r'^issue/channel/(?P<channel_name>\S+?)', 'team.views.channel_detail', name='channel_detail'),
    url(r'^', 'login.views.index'),
]
