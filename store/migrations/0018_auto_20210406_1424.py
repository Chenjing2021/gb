# Generated by Django 3.1.5 on 2021-04-06 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_timeset_remain_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeset',
            name='Remain_time',
        ),
        migrations.RemoveField(
            model_name='timeset',
            name='Start_time',
        ),
    ]
