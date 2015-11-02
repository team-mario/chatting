from django.shortcuts import render, redirect
from .forms import IssueChannelForm
from team.models import IssueChannel
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def index(request):
    # Check limiting access
    if not request.user.is_authenticated():
        return redirect('/accounts/login/')

    issue_channel_form = IssueChannelForm
    return render(request, 'common/base.html', {'issue_channel_form': issue_channel_form,
                                                'issue_channel': IssueChannel.objects.all()})


def channel_create(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        user = request.user
        channel_name = request.POST.get('channel_name')
        channel_content = request.POST.get('channel_content')
        IssueChannel.objects.create(user=user, channel_name=channel_name, channel_content=channel_content)

    return HttpResponseRedirect('../accounts/profile/')


def channel_detail(request, channel_name):
    return redirect('/messages/project-plan')
