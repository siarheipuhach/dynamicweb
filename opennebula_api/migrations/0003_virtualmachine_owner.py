# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-11 09:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opennebula_api', '0002_auto_20170511_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachine',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='virtual_machines', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]