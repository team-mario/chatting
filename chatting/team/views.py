from django.shortcuts import redirect, render
from team.models import Issue, AttachedFile, Team
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from team.forms import IssueForm, TeamForm, UploadFileForm, SearchForm
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
        issue = Issue(issue_name=issue_name, issue_content=issue_content, team=team)
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

    return HttpResponseRedirect('/issue/')


def search_issue(request):
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
