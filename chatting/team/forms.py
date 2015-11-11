from django import forms
from team.models import Issue, Team, AttachedFile, HashTag


class IssueForm(forms.models.ModelForm):
    class Meta:
        model = Issue
        fields = {'issue_name', 'issue_content'}


class UploadFileForm(forms.models.ModelForm):
    class Meta:
        model = AttachedFile
        fields = {'file_name', 'file'}


class SearchForm(forms.Form):
    content = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'search here'}))


class TeamForm(forms.models.ModelForm):
    class Meta:
        model = Team
        fields = {'team_name'}


class HashTagForm(forms.models.ModelForm):
    class Meta:
        model = HashTag
        fields = {'tag_name'}