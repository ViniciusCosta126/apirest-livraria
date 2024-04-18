from rest_framework import viewsets
from ..serializers import AutorSerializer
from ..models import Autor


class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
