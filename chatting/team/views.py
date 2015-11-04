from django.shortcuts import redirect
from team.models import IssueChannel, ChannelFiles, TeamChannel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def channel_create(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        cur_team = request.session['cur_team']
        user_name = request.user.get_username()

        channel_name = request.POST.get('channel_name')
        channel_content = request.POST.get('channel_content')

        team_channel = TeamChannel.objects.get(team_name=cur_team)
        issue_channel = IssueChannel(channel_name=channel_name, channel_content=channel_content, team=team_channel)
        user = User.objects.get(username=user_name)
        issue_channel.user = user
        issue_channel.save()

    return HttpResponseRedirect('/issue/channel/')


@login_required(login_url='/accounts/login/')
def channel_detail(request, channel_name):
    return redirect('/issue/channel/')


@login_required(login_url='/accounts/login/')
def team_detail(request, team_name):
    request.session['cur_team'] = team_name
    return HttpResponseRedirect('/issue/channel/')


@login_required(login_url='/accounts/login/')
def channel_file_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        channel = IssueChannel.objects.get(pk=1)
        ChannelFiles.objects.create(title=title, file=request.FILES['file'], channel=channel)
        return redirect('/accounts/profile/')

    return redirect('/accounts/login/')


def create_room(request):
    if request.method == 'POST':
        team_name = str(request.POST.get('team_name'))
        request.session['cur_team'] = team_name
        TeamChannel.objects.create(team_name=team_name)

    return HttpResponseRedirect('/issue/channel/')
