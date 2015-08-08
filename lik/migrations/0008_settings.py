# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lik', '0007_auto_20150804_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('name', models.CharField(max_length=100, serialize=False, choices=[('phone', 'Телефон'), ('email', 'Электронная почта'), ('sidebar_title', 'Заголовок меню')], primary_key=True)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
    ]
