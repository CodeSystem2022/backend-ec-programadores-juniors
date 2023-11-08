from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category  # Asegúrate de importar tu modelo Category
from rest_framework.permissions import AllowAny
from ..product.models import Product
from .serializers import ProductSerializer

class CategoryList(APIView):
    permission_classes = (AllowAny, )
    
    def get(self, request):
            categories_by_gender = {}
            for gender, _ in Category.GENDER_CHOICES:
                categories = Category.objects.filter(gender=gender)
                category_data = [
                    {
                        'name': category.name,
                        'gender': category.get_gender_display(),  # Obtiene el valor legible del campo de selección
                    }
                    for category in categories
                ]
                categories_by_gender[gender] = category_data
            return Response(categories_by_gender)

class ProductListByGender(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, gender):
        try:
            products = Product.objects.filter(category__gender=gender)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response([], status=status.HTTP_404_NOT_FOUND)

class ProductListByGenderAndCategory(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, name, gender):
        try:
            products = Product.objects.filter(category__gender=gender,category__name=name) 
    
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response([], status=status.HTTP_404_NOT_FOUND)





