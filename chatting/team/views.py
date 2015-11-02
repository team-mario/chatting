from django.shortcuts import render, redirect
from .forms import IssueChannelForm, UploadFileForm
from team.models import IssueChannel, ChannelFiles
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    # Check limiting access
    # if not request.user.is_authenticated():
        # return redirect('/accounts/login/')
    file_channel_form = UploadFileForm
    issue_channel_form = IssueChannelForm
    return render(request, 'common/base.html', {'issue_channel_form': issue_channel_form,
                                                'issue_channel': IssueChannel.objects.all(),
                                                'file_channel_form': file_channel_form})


@login_required(login_url='/accounts/login/')
def channel_create(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        user = request.user
        channel_name = request.POST.get('channel_name')
        channel_content = request.POST.get('channel_content')
        IssueChannel.objects.create(user=user, channel_name=channel_name, channel_content=channel_content)

    return HttpResponseRedirect('../accounts/profile/')


@login_required(login_url='/accounts/login/')
def channel_detail(request, channel_name):
    return redirect('/messages/project-plan')


@login_required(login_url='/accounts/login/')
def channel_file_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        channel = IssueChannel.objects.get(pk=1)
        ChannelFiles.objects.create(title=title, file=request.FILES['file'], channel=channel)
        return redirect('/accounts/profile/')

    return redirect('/accounts/login/')
