#!/virtualenv/lik/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from lik.models import Material, Category, Item, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'order', 'visible']}),
    ]
    list_display = ['name', 'order', 'visible']
    list_display_links = ('name',)
    list_editable = ['order']


class MaterialAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'material', 'date_add')
    list_display_links = ('name',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'material')
    list_display_links = ('name',)


admin.site.register(Material, MaterialAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)