# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 09:43
from __future__ import unicode_literals

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('dateOfBirth', models.DateTimeField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Readings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glucoseLevel', models.DecimalField(decimal_places=4, max_digits=7)),
                ('timePeriod', models.CharField(max_length=50)),
                ('timeOfDay', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(max_length=200)),
                ('medication', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetes.Profile')),
            ],
        ),
    ]
