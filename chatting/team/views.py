from django.shortcuts import redirect
from team.models import IssueChannel, ChannelFiles, RoomChannel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')

def index(request):
    # Check limiting access
    # if not request.user.is_authenticated():
        # return redirect('/accounts/login/')

    issue_channel_form = IssueChannelForm
    room_form = RoomForm
    room_list = RoomChannel.objects.values('room_name').distinct()
    channel_name_list = []

    try:
        cur_room = request.session['cur_room']
        room_q = RoomChannel.objects.get(room_name=cur_room)
        channel_list = room_q.issue_list.split(' ')
        for issue_id in channel_list:
            if issue_id is not None and issue_id is not '':
                integer_id = int(issue_id)
                name = IssueChannel.objects.get(id=integer_id).channel_name
                channel_name_list.append(name)
    except:
        cur_room = 'default'
        name = request.user.get_username()
        RoomChannel.objects.create(room_name=cur_room)
        user_q = User.objects.get(username=name)
        user_q.current_room = cur_room
        request.session['cur_room'] = cur_room

    return render(request, 'common/base.html', {'issue_channel_form': issue_channel_form,
                                                'issue_channel': channel_name_list,
                                                'room_form': room_form,
                                                'room_list': room_list})


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
        issue_channel.save()

        if cur_room is not None:
            room_q = RoomChannel.objects.get(room_name=cur_room)
            room_q.issue_id_id = issue_channel.id

            room_list = room_q.issue_list
            issue_id = str(issue_channel.id)
            result_room = room_list + " " + issue_id
            room_q.issue_list = result_room
            room_q.save()

    return HttpResponseRedirect('/issue/channel/')


@login_required(login_url='/accounts/login/')
def channel_detail(request, channel_name):
    return redirect('/issue/channel/')


@login_required(login_url='/accounts/login/')
def room_detail(request, room_name):
    request.session['cur_room'] = room_name
    return HttpResponseRedirect('/accounts/profile/')


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
        room_name = str(request.POST.get('room_name'))
        name = request.user.get_username()
        RoomChannel.objects.create(room_name=room_name)
        user_q = User.objects.get(username=name)
        user_q.current_room = room_name
        request.session['cur_room'] = room_name

    return HttpResponseRedirect('/issue/channel/')
