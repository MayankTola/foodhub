# Generated by Django 2.2 on 2020-06-02 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_auto_20200602_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 15, 44, 36, 168579)),
        ),
    ]
