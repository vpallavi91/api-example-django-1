# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0002_auto_20170109_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='Date_of_appointment',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='end_time',
        ),
    ]
