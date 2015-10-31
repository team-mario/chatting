from django.db import models
from team.models import IssueChannel


# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=255, default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default=None)
    channel = models.ForeignKey(IssueChannel, default=None)
