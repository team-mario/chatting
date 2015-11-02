# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IssueChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('channel_name', models.CharField(max_length=30)),
                ('channel_content', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None)),
            ],
        ),
        migrations.AddField(
            model_name='HashTag',
            name='channels',
            field=models.ManyToManyField(to='team.IssueChannel'),
        ),
    ]
