# Generated by Django 3.0.7 on 2020-09-30 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200930_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='timesheet',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.EmployeeProfile'),
        ),
    ]
