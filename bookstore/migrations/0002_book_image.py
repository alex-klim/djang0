# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='your wallet is empty'),
        ),
    ]
