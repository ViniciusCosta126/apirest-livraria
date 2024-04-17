from django.contrib import admin
from django.urls import path, include
from livraria_api import urls as livraria_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('livraria/', include(livraria_urls))
]
