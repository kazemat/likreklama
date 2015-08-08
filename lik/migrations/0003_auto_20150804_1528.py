# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0002_auto_20150803_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Элемент', 'verbose_name_plural': 'Элементы'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Материал', 'verbose_name_plural': 'Материалы'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='material',
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.ManyToManyField(to='lik.Material'),
        ),
    ]
