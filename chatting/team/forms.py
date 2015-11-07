from django import forms
from team.models import Issue, Team, AttachedFile


class IssueForm(forms.models.ModelForm):
    class Meta:
        model = Issue
        fields = {'issue_name', 'issue_content'}


class UploadFileForm(forms.models.ModelForm):
    class Meta:
        model = AttachedFile
        fields = {'file_name', 'file'}


class TeamForm(forms.models.ModelForm):
    class Meta:
        model = Team
        fields = {'team_name'}
