from message.models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from team.forms import IssueForm, TeamForm, UploadFileForm, SearchForm
from team.models import Issue, Team
import json
import datetime
from django.shortcuts import get_object_or_404, render


# Create your views here.
def get_messages(request, issue_name=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('../accounts/login/')
    cur_team = ''
    team = ''
    file_form = UploadFileForm
    issue_form = IssueForm
    team_form = TeamForm
    search_form = SearchForm
    teams = Team.objects.values('team_name').distinct()

    default = 'default'

    if 'cur_team' in request.session:
        cur_team = request.session['cur_team']
    else:
        cur_team = default
        request.session['cur_team'] = default

    issue_name_list = []
    issues = ''
    try:
        team = Team.objects.get(team_name=cur_team)
        issues = Issue.objects.filter(team=team.id)
        for issue in issues.all():
            issue_name_list.append(issue)

    except:
        Team.objects.create(team_name=default)

    context = {}
    context['issue_form'] = issue_form
    context['issues'] = issues
    context['team_form'] = team_form
    context['teams'] = teams
    context['file_form'] = file_form
    context['search_form'] = search_form

    if issue_name is not None:
        issue = get_object_or_404(Issue, issue_name=issue_name)
    else:
        return render(
            request,
            'message/default.html',
            context
        )

    messages = []
    received_messages = Message.objects.filter(issue=issue).order_by('id')
    for data in received_messages:
        dic = {}
        dic['message_id'] = data.id
        dic['user_id'] = data.user.id
        dic['username'] = data.user.get_username()
        dic['time'] = data.create_datetime.strftime("%-I:%M %p")
        dic['content'] = data.content
        messages.append(dic)

    if len(received_messages) > 0:
        last_primary_key = received_messages[len(received_messages) - 1].id
        last_send_date = received_messages[0].create_datetime
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


def create_message(request):
    if request.method == 'POST':
        issue_name = request.POST.get('issue_name', None)
        if issue_name is not None:
            issue = Issue.objects.filter(issue_name=issue_name)
            if issue is not None and request.user is not None:
                Message.objects.create(
                    user=request.user,
                    content=request.POST.get('content', ''),
                    issue=issue[0],
                )
                return HttpResponse("inserted")

    return HttpResponse("error request method.")


def get_message(request):
    if request.method == 'GET':
        last_primary_key = request.GET.get('last_primary_key', None)
        issue_name = request.GET.get('issue_name', None)

        if last_primary_key is not None and issue_name is not None:
            messages = []
            last_key = int(last_primary_key)
            issue = Issue.objects.filter(issue_name=issue_name)
            if issue is not None:
                for data in Message.objects.filter(issue=issue, id__gt=last_key).order_by('id'):
                    dic = {}
                    dic['message_id'] = data.id
                    dic['user_id'] = data.user.id
                    dic['username'] = data.user.get_username()
                    dic['time'] = str(data.create_datetime.strftime("%-I:%M %p"))
                    dic['content'] = data.content
                    messages.append(dic)
                messages = json.dumps(messages)
                return HttpResponse(messages, content_type='application/json')

    return HttpResponse("error")
