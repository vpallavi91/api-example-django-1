# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0007_auto_20170112_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time_of_arrival',
            field=models.TimeField(),
        ),
    ]
