from django.db import models


# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=255, default=None)
    datetime = models.DateTimeField(auto_now=True)
    content = models.TextField(default=None)
