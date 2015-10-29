from django.shortcuts import render, redirect
from .forms import IssueChannelForm
from team.models import IssueChannel, UserInfo


def index(request):
    # Suppose I can hold a user session after login success.
    request.session['user_id'] = 'JudeLee'
    if UserInfo.objects.filter(user_id='JudeLee').count() == 1:
        pass
    else:
        UserInfo.objects.create(user_id='JudeLee', user_password='bb')
    issue_channel_form = IssueChannelForm
    return render(request, 'common/base.html', {'issue_channel_form': issue_channel_form, 'issue_channel': IssueChannel.objects.all()})


def channel_create(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        user_info = UserInfo.objects.get(user_id='JudeLee')
        channel_name = request.POST.get('channel_name')
        channel_content = request.POST.get('channel_content')
        IssueChannel.objects.create(user_id=user_info, channel_name=channel_name, channel_content=channel_content)
    return redirect('/')


def channel_detail(request, channel_name):
    return redirect('/messages/project-plan')