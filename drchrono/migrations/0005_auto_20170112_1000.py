# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0004_auto_20170111_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='wait_time',
            field=models.DurationField(null=True),
        ),
    ]
