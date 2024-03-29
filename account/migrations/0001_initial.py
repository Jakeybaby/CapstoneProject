# Generated by Django 3.0.7 on 2020-10-02 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
                ('phone', models.TextField(blank=True, max_length=20, null=True)),
                ('employee_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(blank=True, max_length=25, null=True)),
                ('timeIn', models.DateTimeField(blank=True, null=True)),
                ('timeOut', models.DateTimeField(blank=True, null=True)),
                ('isLast', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.EmployeeProfile')),
            ],
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.GroupEmployee'),
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('phone', models.TextField(blank=True, max_length=100, null=True)),
                ('cus_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
