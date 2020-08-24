# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0011_image_image_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.Profile'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_comments',
            field=models.ManyToManyField(to='insta.Profile'),
        ),
    ]
