# Generated by Django 3.0.8 on 2020-08-21 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20200820_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 8, 21, 13, 57, 31, 387982)),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 8, 21, 13, 57, 31, 387982)),
        ),
    ]
