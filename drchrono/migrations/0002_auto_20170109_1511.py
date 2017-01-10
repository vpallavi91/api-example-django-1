# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='avg_waiting_time',
            field=models.DurationField(null=True),
        ),
    ]
