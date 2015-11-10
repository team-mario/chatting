from django.db import models
from team.models import Issue
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Message(models.Model):
    issue = models.ForeignKey(Issue, default=None)
    user = models.ForeignKey(User, default=None)
    content = models.TextField(default=None)
    create_datetime = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.create_datetime = datetime.now().strftime("%-I:%M %p")
        super(Message, self).save(*args, **kwargs)
