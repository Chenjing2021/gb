# Generated by Django 3.1.5 on 2021-04-10 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_orderitem_date_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='date_ordered',
            new_name='date_added',
        ),
    ]
