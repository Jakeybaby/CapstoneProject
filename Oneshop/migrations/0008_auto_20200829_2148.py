# Generated by Django 3.0.8 on 2020-08-29 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Oneshop', '0007_equipment_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyorder',
            name='data_added',
        ),
        migrations.RemoveField(
            model_name='securityorder',
            name='data_added',
        ),
    ]