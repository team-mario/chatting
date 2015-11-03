from django.shortcuts import render, redirect
from team.models import IssueChannel, ChannelFiles, RoomChannel
from .forms import IssueChannelForm
from django.http import HttpResponseRedirect
from team.forms import RoomForm, IssueChannelForm, UploadFileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def index(request):
    # Check limiting access
    file_channel_form = UploadFileForm
    issue_channel_form = IssueChannelForm
    room_form = RoomForm
    room_list = RoomChannel.objects.values('room_name').distinct()
    request.session['cur_room'] = 'empty'

    return render(request, 'common/base.html', {'issue_channel_form': issue_channel_form,
                                                'issue_channel': IssueChannel.objects.all(),
                                                'room_form': room_form,
                                                'room_list': room_list,
                                                'file_channel_form': file_channel_form})


@login_required(login_url='/accounts/login/')
def channel_create(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        cur_room = request.session['cur_room']
        user_name = request.user.get_username()

        channel_name = request.POST.get('channel_name')
        channel_content = request.POST.get('channel_content')
        issue_channel = IssueChannel(channel_name=channel_name, channel_content=channel_content)
        user = User.objects.get(username=user_name)
        issue_channel.user = user

        if cur_room != 'empty':
            room_q = RoomChannel.objects.get(room_name=cur_room, issue_id=issue_channel.id)
            room_q.save()

        issue_channel.save()

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


def create_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        RoomChannel.objects.create(room_name=room_name)

        name = request.user.get_username()
        user_q = User.objects.get(username=name)
        user_q.current_room = room_name
        request.session['cur_room'] = room_name

    return HttpResponseRedirect('../accounts/profile/')
