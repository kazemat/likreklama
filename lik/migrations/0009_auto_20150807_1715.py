# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0008_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='name',
            field=models.CharField(unique=True, max_length=100, choices=[('phone', 'Телефон'), ('email', 'Электронная почта'), ('sidebar_title', 'Заголовок меню')]),
        ),
    ]
