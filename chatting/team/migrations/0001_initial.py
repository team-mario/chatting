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
            name='ChannelFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='.')),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IssueChannel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('channel_name', models.CharField(max_length=30)),
                ('channel_content', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomChannel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('room_name', models.CharField(default='', max_length=30, unique=True)),
                ('issue_id', models.ForeignKey(default=None, null=True, to='team.IssueChannel')),
            ],
        ),
        migrations.AddField(
            model_name='HashTag',
            name='channels',
            field=models.ManyToManyField(to='team.IssueChannel'),
        ),
        migrations.AddField(
            model_name='channelfiles',
            name='channel',
            field=models.ForeignKey(default=None, to='team.IssueChannel'),
        ),
    ]
