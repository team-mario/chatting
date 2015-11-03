from django import forms
from team.models import IssueChannel, RoomChannel, ChannelFiles


class IssueChannelForm(forms.models.ModelForm):
    class Meta:
        model = IssueChannel
        fields = {'channel_name', 'channel_content'}


class UploadFileForm(forms.models.ModelForm):

    class Meta:
        model = ChannelFiles
        fields = {'title', 'file'}


class RoomForm(forms.models.ModelForm):
    class Meta:
        model = RoomChannel
        fields = {'room_name'}
