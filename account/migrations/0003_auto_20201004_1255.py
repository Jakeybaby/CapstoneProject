# Generated by Django 3.0.7 on 2020-10-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_leave'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='Date',
            new_name='EndDate',
        ),
        migrations.AddField(
            model_name='leave',
            name='StartDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]