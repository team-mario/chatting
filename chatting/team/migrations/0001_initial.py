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
            name='IssueChannel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('channel_name', models.CharField(max_length=30)),
                ('channel_content', models.CharField(default='', max_length=255)),
                ('user', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.CharField(primary_key=True, serialize=False, max_length=20)),
                ('user_password', models.CharField(max_length=30)),
                ('user_email', models.EmailField(default='', max_length=30)),
            ],
        ),
    ]
