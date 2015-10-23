# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssueChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('channel_name', models.CharField(max_length=30)),
                ('channel_content', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.CharField(serialize=False, primary_key=True, max_length=20)),
                ('user_password', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='issuechannel',
            name='user_id',
            field=models.ForeignKey(default=None, to='team.UserInfo'),
        ),
    ]
