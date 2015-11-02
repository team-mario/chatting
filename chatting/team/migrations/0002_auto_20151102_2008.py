# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoomChannel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('room_name', models.CharField(unique=True, max_length=30, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='issuechannel',
            name='user_id',
        ),
        migrations.AddField(
            model_name='issuechannel',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.AddField(
            model_name='roomchannel',
            name='issue_id',
            field=models.ForeignKey(null=True, default=None, to='team.IssueChannel'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='channels',
            field=models.ManyToManyField(to='team.IssueChannel'),
        ),
    ]
