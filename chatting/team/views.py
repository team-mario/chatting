from django.shortcuts import render
from django_modalview.generic.base import ModalTemplateView


def index(request):
    # Suppose I can hold a user session after login success.
    request.session['user_id'] = '11'
    return render(request, 'common/base.html')


class PostIssueForm(ModalTemplateView):
    # model = IssueChannel
    # template_name = 'issue/post_issue_form.html'

    '''
         This modal inherit of ModalTemplateView, so it just display a text without logic.
    '''
    def __init__(self, *args, **kwargs):
        '''
            You have to call the init method of the parent, before to overide the values:
                - title: The title display in the modal-header
                - icon: The css class that define the modal's icon
                - description: The content of the modal.
                - close_button: A button object that has several attributes.(explain below)
        '''
        super(PostIssueForm, self).__init__(*args, **kwargs)
        self.title = "Create a new issue channel."
        self.description = "This is my description"
        self.icon = "icon-mymodal"
