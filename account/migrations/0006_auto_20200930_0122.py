# Generated by Django 3.0.7 on 2020-09-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200929_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='timesheet',
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='timesheet',
            field=models.ManyToManyField(to='account.TimeSheet'),
        ),
    ]
