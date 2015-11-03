from django.db import models
from django.contrib.auth.models import User


class IssueChannel(models.Model):
    user = models.ForeignKey(User, default=None)
    channel_name = models.CharField(max_length=30)
    channel_content = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.channel_name


class HashTag(models.Model):
    channels = models.ManyToManyField(IssueChannel)
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class ChannelFiles(models.Model):
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to='.')
    channel = models.ForeignKey(IssueChannel, default=None)

    def __str__(self):
        return self.title


class RoomChannel(models.Model):
    issue_id = models.ForeignKey(IssueChannel, default=None, null=True)
    room_name = models.CharField(max_length=30, unique=True,
                                 default='', null=False)
