from django.shortcuts import redirect
from team.models import Issue, AttachedFile, Team
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from team.forms import IssueForm, TeamForm, UploadFileForm, SearchForm
from django.shortcuts import render


@login_required(login_url='/accounts/login/')
def create_issue(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        cur_team = request.session['cur_team']
        user_name = request.user.get_username()

        issue_name = request.POST.get('issue_name')
        issue_content = request.POST.get('issue_content')

        team = Team.objects.get(team_name=cur_team)
        issue = Issue(issue_name=issue_name, issue_content=issue_content, team=team, status=0)
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

    group = Group.objects.get(name=team_name)
    request.user.groups.add(group)
    return HttpResponseRedirect('/issue/')


@login_required(login_url='/accounts/login/')
def add_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        issue = Issue.objects.get(pk=1)
        AttachedFile.objects.create(file_name=file_name, file=request.FILES['file'], issue=issue)
        return redirect('/accounts/profile/')

    return redirect('/accounts/login/')


def create_team(request):
    if request.method == 'POST':
        team_name = str(request.POST.get('team_name'))
        request.session['cur_team'] = team_name
        Team.objects.create(team_name=team_name)

        group = Group(name=team_name)
        group.save()
        request.user.groups.add(group)

    return HttpResponseRedirect('/issue/')


def search_issue(request):
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
    try:
        team = Team.objects.get(team_name=current_team)
        issues = Issue.objects.filter(team=team.id)
        for issue in issues.all():
            issue_content = issue.issue_content
            if issue_content.find(str(search_text)) is not -1 and is_empty is False:
                searched_list.append(issue)
    except:
        Team.objects.create(team_name=default)

    print(searched_list)

    context = {}
    context['issue_form'] = issue_form
    context['issues'] = issues
    context['team_form'] = team_form
    context['teams'] = teams
    context['file_form'] = file_form

    context['search_form'] = search_form
    context['searched_list'] = searched_list

    return render(request, 'search/search.html', context)
