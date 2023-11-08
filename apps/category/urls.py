from django.urls import path

from .views import CategoryList, ProductListByGender,  ProductListByGenderAndCategory

urlpatterns = [
    path('', CategoryList.as_view()),
     path('gender/<str:gender>/', ProductListByGender.as_view(), name='product-list-by-gender'),
     path('gender/<str:gender>/<str:name>', ProductListByGenderAndCategory.as_view(), name='product-list-by-gender'),
]