# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchrono', '0008_auto_20170112_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='wait_time',
        ),
    ]
