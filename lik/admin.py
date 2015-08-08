from django.contrib import admin
from lik.models import Material, Category, Item, Product, Settings
# Register your models here.

admin.site.register([Item, Category, Product, Settings])


class MaterialAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]


admin.site.register(Material, MaterialAdmin)