# Generated by Django 3.0.8 on 2020-09-05 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Oneshop', '0012_auto_20200905_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='leash_date',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='return_date',
        ),
    ]