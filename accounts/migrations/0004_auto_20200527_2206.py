# Generated by Django 2.0.1 on 2020-05-27 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200527_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_name',
        ),
    ]