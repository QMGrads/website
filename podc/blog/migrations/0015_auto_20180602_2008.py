# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-02 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180602_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, upload_to='article_image'),
        ),
    ]
