# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0005_auto_20170112_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='id',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
