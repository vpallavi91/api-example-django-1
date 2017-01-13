# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0006_auto_20170112_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_of_arrival',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='wait_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='avg_waiting_time',
            field=models.FloatField(null=True),
        ),
    ]
