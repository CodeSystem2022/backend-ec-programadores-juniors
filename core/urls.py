from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('djoser.urls')), # Djoser Auth URLs
    path('api/', include('apps.user.urls')), # Custom Auth URLs
    path('api/category/', include('apps.category.urls')),
    path('api/product/', include('apps.product.urls')),
    #path('auth/', include('djoser.social.urls')), # Social Auth URLs
]