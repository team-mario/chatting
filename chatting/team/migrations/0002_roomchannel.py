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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('room_name', models.CharField(default='', max_length=30, unique=True)),
                ('issue_id', models.ForeignKey(null=True, to='team.IssueChannel', default=None)),
            ],
        ),
    ]
