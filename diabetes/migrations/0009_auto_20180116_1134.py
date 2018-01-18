# Generated by Django 2.0 on 2018-01-16 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0008_auto_20180116_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caregiver',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients',
            field=models.ManyToManyField(blank=True, related_name='doctors', to='diabetes.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='caregiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='diabetes.Caregiver'),
        ),
    ]