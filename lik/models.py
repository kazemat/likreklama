from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Material(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _('Материал')
        verbose_name_plural = _('Материалы')


class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255, null=True)
    material = models.ForeignKey(Material, null=True)

    def __str__(self):
        return ': '.join([self.name, self.material.name])

    class Meta:
        verbose_name = _('Элемент')
        verbose_name_plural = _('Элементы')


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=255, null=True)
    material = models.ForeignKey(Material, null=True)
    items = models.ManyToManyField(Item, null=True)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Settings(models.Model):
    name = models.CharField(choices=(
        ('phone', 'Телефон'),
        ('email', 'Электронная почта'),
        ('sidebar_title', 'Заголовок меню'),
        ('fax', 'Факс'),
        # ('phone', 'Телефон'),
    ), max_length=100, unique=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return ': '.join([self.name, self.value])


class Page(models.Model):
    name = models.CharField(
        choices=(
            ('main', 'Главная'),
            ('about', 'О компании'),
            ('contacts', 'Контакты')
        ),
        max_length=120
    )
