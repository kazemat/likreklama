#!/virtualenv/lik/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from sorl.thumbnail import get_thumbnail
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Название категории')
    description = models.TextField(max_length=500, null=True, verbose_name=u'Полное описание')
    visible = models.BooleanField(default=True, verbose_name=u'Видимый элемент')
    order = models.IntegerField(verbose_name=u'Порядковый номер', null=True)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _(u'категория')
        verbose_name_plural = _(u'категории')

@python_2_unicode_compatible
class Material(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'Название материала')

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _(u'материал')
        verbose_name_plural = _(u'материалы')

@python_2_unicode_compatible
class Item(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Название компонента')
    material = models.ForeignKey(Material, null=True, verbose_name=u'Материал')

    def __str__(self):
        return ': '.join([self.name, self.material.name])

    class Meta:
        verbose_name = _(u'компонент')
        verbose_name_plural = _(u'компоненты')

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'Название продукта')
    small_description = models.TextField(max_length=150, null=True, verbose_name=u'Краткое описание')
    description = models.TextField(max_length=255, null=True, verbose_name=u'Полное описание продукта')
    date_add = models.DateTimeField(null=True, editable=False, verbose_name=u'Дата создания')
    date_change = models.DateTimeField(auto_now=True, null=True, editable=False, verbose_name=u'Дата изменения')
    material = models.ForeignKey(Material, verbose_name=u'Основной материал')
    items = models.ManyToManyField(Item, verbose_name=u'Компоненты')
    photo = models.ImageField(verbose_name=u'Фотография', null=True)
    category = models.ManyToManyField(Category, verbose_name=u'Категория', null=True)
    thumb = models.ImageField(null=True, editable=False)
    test = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name.capitalize()

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None, **kwargs):
    #     path = self.photo.path
    #     f = open(path)
    #     self.thumb = get_thumbnail(f, '200x200', crop=u'center', quality=99)
    #     f.close()
    #     super(Product, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = _(u'продукт')
        verbose_name_plural = _(u'продукты')
