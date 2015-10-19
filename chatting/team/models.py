from django.db import models


class UserInfo(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_name = models.CharField(max_length=20)