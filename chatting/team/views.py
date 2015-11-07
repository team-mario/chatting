from django.shortcuts import redirect
from django.http import HttpResponse
from team.models import Issue, AttachedFile, Team
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.core.urlresolvers import reverse


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
        AttachedFile.objects.create(file_name=file_name, file=request.FILES['file'], user=user, issue=issue)
        print('멍미')
        print(issue_name)
        return redirect(reverse('issue_detail', kwargs={'issue_name': issue_name}))
        # return HttpResponse('File upload is success')

    return HttpResponse("File upload is failed")


def create_team(request):
    if request.method == 'POST':
        team_name = str(request.POST.get('team_name'))
        request.session['cur_team'] = team_name
        Team.objects.create(team_name=team_name)

    return HttpResponseRedirect('/issue/')


def search_issue(request):
    if request.method == 'POST':
        search_text = request.POST.get('content', None)
        issue = Issue.objects.all()
        result_msg = []
        for content in issue.all():
            value = content.issue_content
            if value.find(str(search_text)) is not -1:
                dic = {}
                dic['issue_name'] = content.issue_name
                result_msg.append(dic)

        result_msg = json.dumps(result_msg)
    return HttpResponse(result_msg, content_type='application/json')
