# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list_l'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='list_l',
            new_name='listt',
        ),
    ]