from django.db import models


class UserInfo(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_password = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30, default='')


class IssueChannel(models.Model):
    user_id = models.ForeignKey(UserInfo, default=None)
    channel_name = models.CharField(max_length=30)
    channel_content = models.CharField(max_length=255, default='')
