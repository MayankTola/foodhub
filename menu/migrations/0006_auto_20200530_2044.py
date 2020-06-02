# Generated by Django 2.2 on 2020-05-30 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200530_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu_details',
            old_name='restaurant_name_id',
            new_name='restaurant',
        ),
        migrations.RemoveField(
            model_name='menu_details',
            name='restaurant_name',
        ),
        migrations.AlterField(
            model_name='order_details',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 20, 43, 51, 271604)),
        ),
    ]