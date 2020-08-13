# Generated by Django 3.0.8 on 2020-08-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200807_2051'),
        ('Oneshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackcusToem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('feedback_order_cusToem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.CustomerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackemTocus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('feedback_order_emTocus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.EmployeeProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AlterField(
            model_name='equiement',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equiement',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.AddField(
            model_name='order',
            name='service_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Oneshop.Services'),
        ),
    ]