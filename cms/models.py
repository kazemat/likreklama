from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField



class Settings(models.Model):
    name = models.CharField(choices=(
        ('phone', 'Телефон'),
        ('email', 'Электронная почта'),
        ('sidebar_title', 'Заголовок меню'),
        ('fax', 'Факс'),
        # ('phone', 'Телефон'),
    ), max_length=14, unique=True, verbose_name='Имя параметра')
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return ': '.join([self.name, self.value])

    class Meta:
        verbose_name = 'настройка'
        verbose_name_plural = 'настройки'


class TextBlock(models.Model):
    name = models.CharField(
        choices=(
            ('main', 'Главная'),
            ('about', 'О компании')
        ),
        max_length=8,
        verbose_name='Название страницы'
    )
    text = RedactorField(max_length=2048, verbose_name='Текст страницы', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блок текста'
        verbose_name_plural = 'блоки текста'


class Email(models.Model):
    address = models.CharField(max_length=120, null=False, verbose_name="Адрес электронной почты")
    description = models.CharField(max_length=300, null=False, verbose_name='Описание адреса')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'адрес электронной почты'
        verbose_name_plural = 'адреса электронной почты'


class Phone(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    description = models.CharField(max_length=300, verbose_name='Описание номер телефона')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'номер телефона'
        verbose_name_plural = 'номера телефонов'


class Contacts(models.Model):
    phone = models.ManyToManyField(Phone, verbose_name='Номера телефонов')
    email = models.ManyToManyField(Email, verbose_name='Адреса электронной почты')
    address = RedactorField(max_length=1024, verbose_name='Адрес', null=False)
    map = models.TextField(max_length=300, verbose_name='Скрипт для карты', null=True)
    description = RedactorField(max_length=1024, verbose_name='Описание маршрута', null=True)
    additional_info = RedactorField(max_length=2048, verbose_name='Дополнительная информация', null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Counter(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')
    script = models.TextField(max_length=2048, verbose_name='Код счетчика')
    visible = models.NullBooleanField(default=False, verbose_name='Видимость', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'счётчик'
        verbose_name_plural = 'счётчики'
