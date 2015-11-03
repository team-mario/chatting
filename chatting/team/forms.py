__author__ = 'judelee'
from django import forms
from team.models import IssueChannel
from team.models import RoomChannel


class IssueChannelForm(forms.models.ModelForm):
    class Meta:
        model = IssueChannel
        fields = {'channel_name', 'channel_content'}


class RoomForm(forms.models.ModelForm):
    class Meta:
        model = RoomChannel
        fields = {'room_name'}
