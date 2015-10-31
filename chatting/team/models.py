from django.db import models
from django.contrib.auth.models import User


class IssueChannel(models.Model):
    user = models.ForeignKey(User, default=None)
    channel_name = models.CharField(max_length=30)
    channel_content = models.CharField(max_length=255, default='')


class HashTag(models.Model):
    channels = models.ManyToManyField(IssueChannel)
    tag_name = models.CharField(max_length=20)
