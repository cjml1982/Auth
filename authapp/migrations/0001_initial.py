# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-26 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, unique=True)),
                ('challenge', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Publickey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32, unique=True)),
                ('key', models.CharField(max_length=512)),
            ],
        ),
    ]
