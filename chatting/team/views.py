from django.shortcuts import redirect, render
from team.models import Issue, AttachedFile, Team, HashTag
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from team.forms import IssueForm, TeamForm, UploadFileForm, SearchForm
from django.http import HttpResponse
import json
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from message.models import Message


@login_required(login_url='/accounts/login/')
def create_issue(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        cur_team = request.session['cur_team']
        user_name = request.user.get_username()

        issue_name = request.POST.get('issue_name')
        issue_content = request.POST.get('issue_content')

        team = Team.objects.get(team_name=cur_team)
        issue = Issue(issue_name=issue_name, issue_content=issue_content, team=team, status="대기중")
        user = User.objects.get(username=user_name)
        issue.user = user
        issue.save()

    return HttpResponseRedirect('/issue/')


@login_required(login_url='/accounts/login/')
def issue_detail(request, issue_name):
    return redirect('/issue/')


@login_required(login_url='/accounts/login/')
def team_detail(request, team_name):
    request.session['cur_team'] = team_name

    return HttpResponseRedirect('/issue/')


@login_required(login_url='/accounts/login/')
def add_file(request):
    if request.method == 'POST':
        user = request.user
        issue_name = request.session.get('issue_name')
        file_name = request.POST.get('file_name')
        issue = Issue.objects.get(issue_name=issue_name)
        created_file = AttachedFile(file_name=file_name, file=request.FILES['file'], user=user, issue=issue)
        created_file.save()

        Message.objects.create(
            user=user,
            content=file_name,
            issue=issue,
            file=created_file
        )
        return redirect(reverse('issue_detail', kwargs={'issue_name': issue_name}))
        # return HttpResponse('File upload is success')
        # return redirect('/message/get', kwargs={'issue_name': issue_name})

    return HttpResponse("File upload is failed")


@login_required(login_url='/accounts/login')
def add_hash_tag(request):
    if request.method == 'POST':
        issue_name = request.session.get('issue_name')
        issue = Issue.objects.get(issue_name=issue_name)
        tag_name = request.POST.get('tag_name')

        hash_tag = HashTag.objects.filter(tag_name=tag_name)
        if hash_tag.count() > 0:
            hash_tag[0].issues.add(issue)
        else:
            created_hash_tag = HashTag(tag_name=tag_name)
            created_hash_tag.save()
            created_hash_tag.issues.add(issue)

        return redirect(reverse('issue_detail', kwargs={'issue_name': issue_name}))

    return HttpResponse('Adding Hash Tag is failed')


def send_file(request, id):
    file_obj = AttachedFile.objects.get(id=id)
    response = HttpResponse()
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="%s"' % file_obj.file_name
    with open(file_obj.file.path, 'rb') as file_p:
        response.write(file_p.read())

    return response


def create_team(request):
    if request.method == 'POST':
        team_name = str(request.POST.get('team_name'))
        request.session['cur_team'] = team_name
        Team.objects.create(team_name=team_name)

        user = User.objects.get(username=request.user)
        group = Group(name=team_name)
        group.save()
        group.user_set.add(user)

    return HttpResponseRedirect('/issue/')


def search_issue(request):
    file_form = UploadFileForm
    issue_form = IssueForm
    team_form = TeamForm
    search_form = SearchForm

    default = 'default'
    search_text = request.POST.get('content', None)
    my_teams = request.user.groups.all()

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
    try:
        team = Team.objects.get(team_name=current_team)
        issues = Issue.objects.filter(team=team.id)
        for issue in issues.all():
            issue_content = issue.issue_content
            if issue_content.find(str(search_text)) is not -1 and is_empty is False:
                searched_list.append(issue)
    except:
        Team.objects.create(team_name=default)

    context = {}
    context['issue_form'] = issue_form
    context['issues'] = issues
    context['team_form'] = team_form
    context['file_form'] = file_form
    context['search_form'] = search_form
    context['searched_list'] = searched_list
    context['my_teams'] = my_teams

    return render(request, 'search/search.html', context)


def invite_user(request):
    if request.method == 'POST':
        team_name = str(request.POST.get('team'))
        invited_user = str(request.POST.get('user'))

        user = User.objects.get(username=invited_user)
        group = Group.objects.get(name=team_name)
        group.user_set.add(user)

    return HttpResponseRedirect('/issue/')


def get_users(request):
    if request.method == 'POST':
        team_name = str(request.POST.get('team'))
        user_list = User.objects.filter(groups__name=team_name)
        is_valid = False

        invite_user = []
        if user_list.exists() is False:
            for user in User.objects.all():
                if user != request.user:
                    dic = {}
                    dic['user'] = str(user)
                    invite_user.append(dic)
        else:
            for user in User.objects.all():
                for team_user in user_list.all():
                    if user != team_user:
                        is_valid = True
                    else:
                        is_valid = False
                        break

                if is_valid is True and user is not request.user:
                    dic = {}
                    dic['user'] = str(user)
                    invite_user.append(dic)

        invite_user = json.dumps(invite_user)

    return HttpResponse(invite_user, content_type='application/json')
