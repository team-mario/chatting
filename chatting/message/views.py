from message.models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from team.forms import IssueChannelForm, RoomForm, UploadFileForm
from team.models import IssueChannel, RoomChannel
import json
import datetime
from django.shortcuts import get_object_or_404, render


# Create your views here.
def message_list(request, channel_name=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('../accounts/login/')

    file_channel_form = UploadFileForm
    issue_channel_form = IssueChannelForm
    room_form = RoomForm
    room_list = RoomChannel.objects.values('room_name').distinct()
    request.session['cur_room'] = 'empty'

    context = {}
    context['issue_channel_form'] = issue_channel_form
    context['issue_channel'] = IssueChannel.objects.all()
    context['room_form'] = room_form
    context['room_list'] = room_list
    context['file_channel_form'] = file_channel_form
    if channel_name is not None:
        issue = get_object_or_404(IssueChannel, channel_name=channel_name)
    else:
        return render(
            request,
            'message/default.html',
            context
        )

    messages = []
    messages_list = Message.objects.filter(issue=issue).order_by('id')

    for data in messages_list:
            dic = {}
            dic['sender'] = data.sender
            dic['time'] = data.create_datetime.strftime("%-I:%M %p")
            dic['content'] = data.content
            messages.append(dic)

    if len(messages_list) > 0:
        last_primary_key = messages_list[len(messages_list) - 1].id
        last_send_date = messages_list[0].create_datetime
    else:
        last_primary_key = 0
        last_send_date = datetime.datetime.today()

    context['issue'] = issue
    context['messages'] = messages
    context['last_primary_key'] = last_primary_key
    context['last_send_date'] = last_send_date

    return TemplateResponse(
        request,
        'message/list.html',
        context
    )


def message_create(request):
    request.method = 'POST'
    if request.method == 'POST':
        channel_name = request.POST.get('channel_name', None)
        if channel_name is not None:
            issue = IssueChannel.objects.filter(channel_name=channel_name)
            if issue is not None:
                Message.objects.create(
                    sender=request.POST.get('sender', ''),
                    content=request.POST.get('content', ''),
                    issue=issue[0],
                )
                return HttpResponse("inserted")

    return HttpResponse("error request method.")


def message_receive(request):
    if request.method == 'GET':
        last_primary_key = request.GET.get('last_primary_key', None)
        channel_name = request.GET.get('channel_name', None)

        if last_primary_key is not None and channel_name is not None:
            messages = []
            last_key = int(last_primary_key)
            issue = IssueChannel.objects.filter(channel_name=channel_name)
            if issue is not None:
                for data in Message.objects.filter(issue=issue, id__gt=last_key).order_by('id'):
                        dic = {}
                        dic['id'] = data.id
                        dic['sender'] = data.sender
                        dic['time'] = str(data.create_datetime.strftime("%-I:%M %p"))
                        dic['content'] = data.content
                        messages.append(dic)
                messages = json.dumps(messages)
                return HttpResponse(messages, content_type='application/json')

    return HttpResponse("error")
