from django.shortcuts import render
from message.models import Message
from django.http import HttpResponse
import json
import datetime


# Create your views here.
def message_list(request):
    messages = []
    messages_list = Message.objects.all().order_by('id')
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

    context = {
        'messages': messages,
        'last_primary_key': last_primary_key,
        'last_send_date': last_send_date,
    }

    return render(
        request,
        'message/list.html',
        context
    )


def message_create(request):
    if request.method == 'POST':
        Message.objects.create(
            sender=request.POST.get('sender', ''),
            content=request.POST.get('content', ''),
        )
        return HttpResponse("inserted")

    return HttpResponse("error")


def message_receive(request):
    if request.method == 'GET':
        last_primary_key = request.GET.get('last_primary_key', None)

        if last_primary_key is not None:
            messages = []
            last_key = int(last_primary_key)
            for data in Message.objects.filter(id__gt=last_key).order_by('id'):
                    dic = {}
                    dic['id'] = data.id
                    dic['sender'] = data.sender
                    dic['time'] = \
                        str(data.create_datetime.strftime("%-I:%M %p"))
                    dic['content'] = data.content
                    messages.append(dic)
            messages = json.dumps(messages)
            return HttpResponse(messages, content_type='application/json')

    return HttpResponse("error")
