from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    team_name = models.CharField(max_length=30, unique=True)


class Issue(models.Model):
    user = models.ForeignKey(User, default=None)
    team = models.ForeignKey(Team, default=None)
    issue_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    issue_content = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.issue_name


class HashTag(models.Model):
    issues = models.ManyToManyField(Issue)
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class AttachedFile(models.Model):
    file_name = models.CharField(max_length=30)
    file = models.FileField(upload_to='.')
    issue = models.ForeignKey(Issue, default=None)

    def __str__(self):
        return self.file_name
