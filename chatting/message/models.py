from django.db import models
from team.models import IssueChannel


# Create your models here.
class Message(models.Model):
    issue = models.ForeignKey(IssueChannel, default=None)
    sender = models.CharField(max_length=255, default=None)
    content = models.TextField(default=None)
    create_datetime = models.DateTimeField(auto_now_add=True)
