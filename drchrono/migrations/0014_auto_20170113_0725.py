# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0013_appointment_wait_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='wait_time',
            field=models.IntegerField(null=True),
        ),
    ]
