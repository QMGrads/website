# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-01 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=100)),
                ('Article', models.CharField(max_length=10000)),
            ],
        ),
    ]
