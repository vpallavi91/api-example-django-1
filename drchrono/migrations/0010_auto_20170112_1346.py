# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0009_remove_appointment_wait_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='avg_waiting_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='total_patients',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='total_wait_time',
            field=models.IntegerField(null=True),
        ),
    ]
