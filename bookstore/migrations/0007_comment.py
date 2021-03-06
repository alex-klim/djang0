# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 00:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20171025_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='cold-hearted machine', max_length=25)),
                ('comment', models.TextField(max_length=300)),
                ('mark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Book')),
            ],
        ),
    ]
