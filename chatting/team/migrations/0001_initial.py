# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
    ]
