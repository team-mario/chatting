from message.models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from team.forms import IssueForm, TeamForm, UploadFileForm, SearchForm, HashTagForm
from team.models import Issue, Team, HashTag
import json
import datetime


# Create your views here.
def get_messages(request, issue_name=None):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('../accounts/login/')
    file_form = UploadFileForm
    hash_tag_form = HashTagForm
    issue_form = IssueForm
    team_form = TeamForm
    search_form = SearchForm

    default = 'default'

    request.session['issue_name'] = issue_name

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

    user_list = User.objects.filter(groups__name=cur_team)
    my_teams = request.user.groups.all()

    if cur_team == default:
        issues = None

    context = {}
    context['issue_form'] = issue_form
    context['issues'] = issues
    context['team_form'] = team_form
    context['file_form'] = file_form
    context['hash_tag_form'] = hash_tag_form
    context['search_form'] = search_form
    context['user_list'] = user_list
    context['my_teams'] = my_teams

    if issue_name is not None:
        issue = get_object_or_404(Issue, team=team, issue_name=issue_name)
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
        dic['file'] = data.file

        messages.append(dic)

    if len(received_messages) > 0:
        last_primary_key = received_messages[len(received_messages) - 1].id
        last_send_date = received_messages[0].create_datetime
    else:
        last_primary_key = 0
        last_send_date = datetime.datetime.today()

    hash_tags = []
    added_hash_tags = HashTag.objects.filter(issues=issue).order_by('id')
    for data in added_hash_tags:
        dic = {}
        dic['hash_tag_id'] = data.id
        dic['hash_tag_name'] = data.tag_name
        hash_tags.append(dic)

    context['issue'] = issue
    context['messages'] = messages
    context['hash_tags'] = hash_tags
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
        if 'cur_team' in request.session:
            cur_team = request.session['cur_team']
            team = Team.objects.get(team_name=cur_team)
        if issue_name is not None:
            issue = Issue.objects.filter(issue_name=issue_name, team=team)
            if issue is not None and request.user is not None:
                Message.objects.create(
                    user=request.user,
                    content=request.POST.get('content', ''),
                    issue=issue[0],
                )
                # Adding hash tag in message contents.
                content_list = request.POST.get('content', '')
                content_list = content_list.split(' ')
                for content in content_list:
                    if content.find("#") != -1:
                        splited_content = content.split('#')
                        hash_tag = HashTag.objects.filter(tag_name=splited_content[1])
                        if hash_tag.count() > 0:
                            hash_tag[0].issues.add(issue[0])
                        else:
                            created_hash_tag = HashTag(tag_name=splited_content[1])
                            created_hash_tag.save()
                            created_hash_tag.issues.add(issue[0])

                return HttpResponse("insert_success")
            return HttpResponse("not found issue or user")
        return HttpResponse("not found issue name")
    return HttpResponse("error request method.")


def get_message(request):
    if request.method == 'GET':
        last_primary_key = request.GET.get('last_primary_key', None)
        issue_name = request.GET.get('issue_name', None)

        if last_primary_key is not None and issue_name is not None:
            messages = []
            last_key = int(last_primary_key)
            if 'cur_team' in request.session:
                cur_team = request.session['cur_team']

            team = Team.objects.get(team_name=cur_team)
            issue = Issue.objects.filter(issue_name=issue_name, team=team)
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


def change_status(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        assignment = request.POST.get('assignment')
        issue_name = request.POST.get('issue')
        current_team = request.session['cur_team']

        team = Team.objects.filter(team_name=current_team)
        user = User.objects.get(username=assignment)
        Issue.objects.filter(issue_name=issue_name, team=team).update(user=user, status=status)
        return redirect('/accounts/profile/')
    return redirect('/accounts/login/')


def show_issues(request):
    current_team = ''
    file_form = UploadFileForm
    issue_form = IssueForm
    team_form = TeamForm
    search_form = SearchForm
    teams = Team.objects.values('team_name').distinct()

    default = 'default'
    search_text = request.POST.get('content', None)

    if not search_text:
        is_empty = True
    else:
        is_empty = False

    if 'cur_team' in request.session:
        current_team = request.session['cur_team']
    else:
        current_team = default
        request.session['cur_team'] = default

    searched_list = []
    issues = ''
    waiting = []
    complete = []
    fixing = []
    user_list = ''
    my_teams = request.user.groups.all()

    try:
        team = Team.objects.filter(team_name=current_team)
        issues = Issue.objects.filter(team=team)
        user_list = User.objects.filter(groups__name=current_team)

        for issue in issues.all():
            issue_content = issue.issue_content
            if issue.status == "대기중":
                waiting.append(issue)
            elif issue.status == "수정중":
                fixing.append(issue)
            elif issue.status == "완료":
                complete.append(issue)

            if issue_content.find(str(search_text)) is not -1 and is_empty is False:
                searched_list.append(issue)
    except:
        Team.objects.create(team_name=default)

    if current_team == default:
        issues = None

    context = {}
    context['issue_form'] = issue_form
    context['issues'] = issues
    context['team_form'] = team_form
    context['teams'] = teams
    context['file_form'] = file_form
    context['search_form'] = search_form
    context['searched_list'] = searched_list
    context['user_list'] = user_list
    context['my_teams'] = my_teams
    context['waiting'] = waiting
    context['fixing'] = fixing
    context['complete'] = complete

    return render(
        request,
        'message/issues.html',
        context
    )
