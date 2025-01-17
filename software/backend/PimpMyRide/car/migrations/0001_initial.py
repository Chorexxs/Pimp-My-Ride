# Generated by Django 5.1.4 on 2025-01-17 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('is_on', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
    ]
