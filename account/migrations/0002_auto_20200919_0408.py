# Generated by Django 3.0.7 on 2020-09-19 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organism',
            name='kingdom',
        ),
        migrations.DeleteModel(
            name='Kingdom',
        ),
        migrations.DeleteModel(
            name='Organism',
        ),
    ]
