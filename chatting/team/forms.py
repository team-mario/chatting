from django import forms
from team.models import IssueChannel, TeamChannel, ChannelFiles


class IssueChannelForm(forms.models.ModelForm):
    class Meta:
        model = IssueChannel
        fields = {'channel_name', 'channel_content'}


class UploadFileForm(forms.models.ModelForm):

    class Meta:
        model = ChannelFiles
        fields = {'title', 'file'}


class TeamForm(forms.models.ModelForm):
    class Meta:
        model = TeamChannel
        fields = {'team_name'}
