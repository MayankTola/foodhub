# Generated by Django 2.2 on 2020-05-30 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20200530_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 21, 5, 59, 737247)),
        ),
    ]
