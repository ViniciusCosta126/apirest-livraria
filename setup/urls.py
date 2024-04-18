from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from livraria_api.views import CategoriaViewSet, AutorViewSet, LivroViewSet
router = routers.DefaultRouter()

router.register('categorias', CategoriaViewSet)
router.register('autores', AutorViewSet)
router.register('livros', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
