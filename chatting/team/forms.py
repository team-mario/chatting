__author__ = 'judelee'
from django import forms
from team.models import IssueChannel, ChannelFiles


class IssueChannelForm(forms.models.ModelForm):
    # channel_name = forms.CharField(label='Channel Name', max_length=30)
    # channel_content = forms.CharField(label='Purpose(Optional)', max_length=255)
    class Meta:
        model = IssueChannel
        fields = {'channel_name', 'channel_content'}


class UploadFileForm(forms.models.ModelForm):

    class Meta:
        model = ChannelFiles
        fields = {'title', 'file'}

