# Generated by Django 2.2 on 2020-05-30 11:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_details',
            name='description',
            field=models.TextField(blank=True, default='No Description', max_length=5000),
        ),
        migrations.AlterField(
            model_name='menu_details',
            name='restaurant_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order_details',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 30, 16, 44, 48, 634792)),
        ),
    ]
