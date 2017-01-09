# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_id', models.IntegerField()),
                ('Date_of_appointment', models.DateField()),
                ('time_of_arrival', models.TimeField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('wait_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctor_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('avg_waiting_time', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(to='drchrono.Doctor'),
        ),
    ]
