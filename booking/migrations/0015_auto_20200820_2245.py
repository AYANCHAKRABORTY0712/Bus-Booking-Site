# Generated by Django 3.0.8 on 2020-08-20 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20200820_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='route',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 8, 20, 22, 45, 35, 967031)),
        ),
        migrations.AlterField(
            model_name='bus',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2020, 8, 20, 22, 45, 35, 967030)),
        ),
    ]
