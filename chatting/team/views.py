from django.shortcuts import render
from .forms import IssueChannelForm


def index(request):
    # Suppose I can hold a user session after login success.
    # request.session['user_id'] = '11'
    issue_channel_form = IssueChannelForm
    return render(request, 'common/base.html', {'issue_channel_form': issue_channel_form})

