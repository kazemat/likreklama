from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from sorl.thumbnail import get_thumbnail


class Category(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название категории')
    description = models.TextField(max_length=500, null=True, verbose_name='Полное описание')
    visible = models.BooleanField(default=True, verbose_name='Видимый элемент')
    order = models.IntegerField(verbose_name='Порядковый номер', null=True)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _('категория')
        verbose_name_plural = _('категории')


class Material(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название материала')

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _('материал')
        verbose_name_plural = _('материалы')


class Item(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название компонента')
    material = models.ForeignKey(Material, null=True, verbose_name='Материал')

    def __str__(self):
        return ': '.join([self.name, self.material.name])

    class Meta:
        verbose_name = _('компонент')
        verbose_name_plural = _('компоненты')


class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название продукта')
    small_description = models.TextField(max_length=150, null=True, verbose_name='Краткое описание')
    description = models.TextField(max_length=255, null=True, verbose_name='Полное описание продукта')
    date_add = models.DateTimeField(null=True, editable=False, verbose_name='Дата создания')
    date_change = models.DateTimeField(auto_now=True, null=True, editable=False, verbose_name='Дата изменения')
    material = models.ForeignKey(Material, verbose_name='Основной материал')
    items = models.ManyToManyField(Item, verbose_name='Компоненты')
    photo = models.ImageField(verbose_name='Фотография', null=True)
    category = models.ManyToManyField(Category, verbose_name='Категория', null=True)
    thumb = models.ImageField(null=True, editable=False)
    test = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.name.capitalize()

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None, **kwargs):
    #     path = self.photo.path
    #     f = open(path)
    #     self.thumb = get_thumbnail(f, '200x200', crop='center', quality=99)
    #     f.close()
    #     super(Product, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = _('продукт')
        verbose_name_plural = _('продукты')
