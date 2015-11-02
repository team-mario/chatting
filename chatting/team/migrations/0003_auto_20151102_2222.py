# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_channelfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelfiles',
            name='file',
            field=models.FileField(upload_to='.'),
        ),
    ]
