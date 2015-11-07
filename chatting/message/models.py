from django.db import models
from team.models import Issue
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    issue = models.ForeignKey(Issue, default=None)
    user = models.ForeignKey(User, default=None)
    content = models.TextField(default=None)
    create_datetime = models.DateTimeField(auto_now_add=True)
