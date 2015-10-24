from django.db import models


class User(models.Model):

    name = models.CharField(default='', max_length='25')
    password = models.CharField(default='', max_length='25')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.text
