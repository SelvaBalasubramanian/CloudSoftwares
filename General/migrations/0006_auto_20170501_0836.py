# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0005_auto_20170501_0832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='softwares',
            old_name='specification',
            new_name='requirements',
        ),
        migrations.AddField(
            model_name='softwares',
            name='cover_pic',
            field=models.FileField(default='software-icon-30.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='users',
            name='pro_pic',
            field=models.FileField(default='default.jpg', upload_to=''),
        ),
    ]