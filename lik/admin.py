from django.contrib import admin
from lik.models import Material, Category, Item, Product
# Register your models here.

admin.site.register([Category])


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