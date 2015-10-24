# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True,
                 auto_created=True, verbose_name='ID', serialize=False)),
                ('sender', models.CharField(max_length=255, default=None)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(default=None)),
            ],
        ),
    ]
