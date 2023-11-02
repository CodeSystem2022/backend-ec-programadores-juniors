from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'description', 'price', 'compare_price', 'category', 'quantity', 'sold', 'date_created')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Product, ProductAdmin)