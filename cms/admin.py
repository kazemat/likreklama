#!/virtualenv/lik/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from cms.models import Settings, TextBlock, Email, Phone, Contacts, Counter
from .models import models
from redactor.fields import RedactorEditor


class SettingsModel(admin.ModelAdmin):
    list_display = ('name', 'value')
    list_display_links = ('name',)


admin.site.register(Settings, SettingsModel)


class TextBlockAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'description')
    list_display_links = ('address', )


class CounterAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible')
    list_display_links = ('name',)


admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(Contacts, ContactAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register([Email, Phone])