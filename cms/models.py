#!/virtualenv/lik/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Settings(models.Model):
    name = models.CharField(choices=(
        ('phone', u'Телефон'),
        ('email', u'Электронная почта'),
        ('sidebar_title', u'Заголовок меню'),
        ('fax', u'Факс'),
        # ('phone', 'Телефон'),
    ), max_length=14, unique=True, verbose_name=u'Имя параметра')
    value = models.CharField(max_length=255, verbose_name=u'Значение')

    def __str__(self):
        return ': '.join([self.name, self.value])

    class Meta:
        verbose_name = u'настройка'
        verbose_name_plural = u'настройки'

@python_2_unicode_compatible
class TextBlock(models.Model):
    name = models.CharField(
        choices=(
            ('main', u'Главная'),
            ('about', u'О компании')
        ),
        max_length=8,
        verbose_name=u'Название страницы'
    )
    text = RedactorField(max_length=2048, verbose_name=u'Текст страницы', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'блок текста'
        verbose_name_plural = u'блоки текста'

@python_2_unicode_compatible
class Email(models.Model):
    address = models.CharField(max_length=120, null=False, verbose_name=u"Адрес электронной почты")
    description = models.CharField(max_length=300, null=False, verbose_name=u'Описание адреса')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = u'адрес электронной почты'
        verbose_name_plural = u'адреса электронной почты'

@python_2_unicode_compatible
class Phone(models.Model):
    phone = models.CharField(max_length=20, verbose_name=u'Номер телефона')
    description = models.CharField(max_length=300, verbose_name=u'Описание номер телефона')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = u'номер телефона'
        verbose_name_plural = u'номера телефонов'

@python_2_unicode_compatible
class Contacts(models.Model):
    phone = models.ManyToManyField(Phone, verbose_name=u'Номера телефонов')
    email = models.ManyToManyField(Email, verbose_name=u'Адреса электронной почты')
    address = RedactorField(max_length=1024, verbose_name=u'Адрес', null=False)
    map = models.TextField(max_length=300, verbose_name=u'Скрипт для карты', null=True)
    description = RedactorField(max_length=1024, verbose_name=u'Описание маршрута', null=True)
    additional_info = RedactorField(max_length=2048, verbose_name=u'Дополнительная информация', null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = u'контакты'
        verbose_name_plural = u'контакты'

@python_2_unicode_compatible
class Counter(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Название')
    script = models.TextField(max_length=2048, verbose_name=u'Код счетчика')
    visible = models.NullBooleanField(default=False, verbose_name=u'Видимость', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'счётчик'
        verbose_name_plural = u'счётчики'
