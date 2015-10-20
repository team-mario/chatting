from django.db import models
from django.core.urlresolvers import reverse


class UserInfo(models.Model):

    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

    def __repr__(self):
        return '<UserInfo %s>' % self.user_name


