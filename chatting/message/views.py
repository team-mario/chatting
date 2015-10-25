from django.shortcuts import render
from message.models import Message
from django.http import HttpResponse
import json


# Create your views here.
def message_list(request):
    messages = []
    for data in Message.objects.all().order_by('id'):
            dic = {}
            dic['sender'] = data.sender
            dic['datetime'] = data.datetime
            dic['content'] = data.content
            messages.append(dic)

    last_primary_key = Message.objects.last().id

    context = {
        'messages': messages,
        'last_primary_key': last_primary_key,
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
                    dic['datetime'] = str(data.datetime)
                    dic['content'] = data.content
                    messages.append(dic)
            messages = json.dumps(messages)
            return HttpResponse(messages, content_type='application/json')

    return HttpResponse("error")
