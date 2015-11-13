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
    url(r'^message/create$', 'message.views.create_message'),
    url(r'^message/get$', 'message.views.get_message'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/accounts/login/'}),
    url(r'^accounts/registration/$', 'login.views.registration'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/change_password/$', 'django.contrib.auth.views.password_change',
        {'post_change_redirect': 'message.views.get_messages'}),
    url(r'^password_change/done/$',
        'django.contrib.auth.views.password_change_done'),
    url(r'^issue/create$', 'team.views.create_issue', name='create_issue'),
    url(r'^issue/$', 'message.views.get_messages'),
    url(r'^issue/file/add$', 'team.views.add_file'),
    url(r'^issue/list$', 'message.views.show_issues'),
    url(r'^issue/change$', 'message.views.change_status'),
    url(r'^issue/hash_tag/add$', 'team.views.add_hash_tag'),
    url(r'^media/(?P<id>\S+)', 'team.views.send_file', name='send_file'),
    url(r'^issue/(?P<issue_name>[\w-]+)', 'message.views.get_messages', name='issue_detail'),
    url(r'^team/create', 'team.views.create_team'),
    url(r'^team/get_users', 'team.views.get_users'),
    url(r'^team/search$', 'team.views.search_issue'),
    url(r'^team/invite', 'team.views.invite_user'),
    url(r'^team/detail/(?P<team_name>\S+)', 'team.views.team_detail'),
    url(r'^', 'login.views.index'),
]
