# Generated by Django 3.0.8 on 2020-08-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oneshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accept'), ('D', 'Finish')], default='Pending', max_length=1),
            preserve_default=False,
        ),
    ]
