from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('djoser.urls')), # Djoser Auth URLs
    path('api/', include('apps.user.urls')), # Custom Auth URLs
    path('api/category/', include('apps.category.urls')),
    path('api/product/', include('apps.product.urls')),
    path('api/payment/', include('apps.payment.urls')),
    #path('auth/', include('djoser.social.urls')), # Social Auth URLs
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)