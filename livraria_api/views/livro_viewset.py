from rest_framework import viewsets
from ..serializers import LivroSerializer
from ..models import Livro


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
