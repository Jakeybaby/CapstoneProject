# Generated by Django 3.0.7 on 2020-09-28 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oneshop', '0005_propetyservices_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propetyservices',
            name='test',
            field=models.DateField(blank=True, null=True),
        ),
    ]
