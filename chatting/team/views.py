from django.shortcuts import render
from django.views.generic import UpdateView
# from django_modalview.generic.base import ModalTemplateView


def index(request):
    # Suppose I can hold a user session after login success.
    # request.session['user_id'] = '11'
    return render(request, 'common/base.html')


class PostIssueForm(UpdateView):
    pass

'''
class PostIssueForm(ModalTemplateView):
    # model = IssueChannel
    # template_name = 'issue/post_issue_form.html'
    pass
'''
