# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0010_auto_20170112_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
