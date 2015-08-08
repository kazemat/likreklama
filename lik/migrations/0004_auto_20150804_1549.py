# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0003_auto_20150804_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.RemoveField(
            model_name='item',
            name='material',
        ),
        migrations.AddField(
            model_name='item',
            name='material',
            field=models.ForeignKey(to='lik.Material'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='items',
            field=models.ManyToManyField(to='lik.Item'),
        ),
    ]
