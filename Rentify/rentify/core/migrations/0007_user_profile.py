# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-10 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Profile',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]