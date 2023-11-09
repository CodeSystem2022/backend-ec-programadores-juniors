from django.db import models
from datetime import datetime
from apps.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=1000)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)
    
    # Campo para los tamaños/talles
    sizes = models.CharField(max_length=100, blank=True, null=True)

    def get_thumbnail(self):
        if self.photo:
            return self.photo.url
        return ''

    def __str__(self):
        return self.name

    def available_sizes(self):
        if self.category.name == 'indumentaria':
            return ['S', 'M', 'L', 'XL']
        elif self.category.name == 'calzado':
            return ['6','7','7.5','8', '8.5', '9', '9.5','10','10.5','11','12']  # Agrega más tamaños si es necesario para calzado
        else:
            return []

