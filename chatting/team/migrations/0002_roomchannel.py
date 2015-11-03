# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomChannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=30, unique=True, default='')),
                ('issue_list', models.TextField(null=True, default='')),
                ('issue_id', models.ForeignKey(default=None, to='team.IssueChannel', null=True)),
            ],
        ),
    ]
