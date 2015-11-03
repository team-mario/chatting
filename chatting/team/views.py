from team.models import IssueChannel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def channel_create(request):
    if request.method == 'POST':
        # Below codes needs code refactoring.
        user = request.user
        channel_name = request.POST.get('channel_name')
        channel_content = request.POST.get('channel_content')
        IssueChannel.objects.create(user=user, channel_name=channel_name, channel_content=channel_content)

    return HttpResponseRedirect('../issue/channel/')
