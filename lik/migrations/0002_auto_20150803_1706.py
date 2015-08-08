# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.TextField(max_length=30),
        ),
    ]
