# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-14 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(default=''),
        ),
    ]