# Generated by Django 5.0.6 on 2024-06-20 06:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelTech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='ad',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='pa',
            field=models.CharField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]
