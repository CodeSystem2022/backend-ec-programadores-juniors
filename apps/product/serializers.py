from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    sizes = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_sizes(self, obj):
        # Lógica para determinar los tamaños/talles disponibles según la categoría
        if obj.category.name == 'Indumentaria':
            return ['S', 'M', 'L', 'XL']
        elif obj.category.name == 'Calzado':
            return ['6','7','7.5','8', '8.5', '9', '9.5','10','10.5','11','12']  # Agrega más tamaños si es necesario para calzado
        else:
            return []
