# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0006_auto_20150804_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='items',
            field=models.ManyToManyField(to='lik.Item', null=True),
        ),
    ]
