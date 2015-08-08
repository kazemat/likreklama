# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0004_auto_20150804_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(null=True, to='lik.Material'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='material',
            field=models.ForeignKey(null=True, to='lik.Material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='items',
            field=models.ManyToManyField(null=True, to='lik.Item'),
        ),
    ]
