from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'sold', 'date_created')
    list_filter = ('category', 'date_created')
    search_fields = ('name', 'description')
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('name', 'photo', 'description', 'price', 'category', 'quantity', 'sold', 'date_created')
        }),
         ('Sizes', {
            'fields': ('sizes',),
            'classes': ('collapse',),  # Colapsar el bloque "Sizes" para mostrarlo opcionalmente
        }),
    )

    def available_sizes(self, obj):
        return ', '.join(obj.available_sizes())  # Utiliza el método definido en el modelo

    available_sizes.short_description = 'Available Sizes'  # Nombre de la columna en la lista de productos

admin.site.register(Product, ProductAdmin)
