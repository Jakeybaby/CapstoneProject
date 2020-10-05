# Generated by Django 3.0.7 on 2020-10-04 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.EmployeeProfile')),
            ],
        ),
    ]
