__author__ = 'judelee'
from django import forms


class IssueChannelForm(forms.Form):
    channel_name = forms.CharField(label='Channel Name', max_length=30)
    channel_content = forms.CharField(label='Purpose(Optional)', max_length=255)

