# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20161229_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contractFile',
            field=models.FileField(null=True, upload_to='media/user_contract'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='resume',
            field=models.FileField(null=True, upload_to='media/user_resume'),
        ),
    ]
