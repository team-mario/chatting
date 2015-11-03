# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_roomchannel'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomchannel',
            name='issue_list',
            field=models.TextField(null=True, default=''),
        ),
    ]
