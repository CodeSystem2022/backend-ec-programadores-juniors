from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
    list_filter = ('gender',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

