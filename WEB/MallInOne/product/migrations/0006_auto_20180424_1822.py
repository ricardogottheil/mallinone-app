# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_local'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reference',
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
