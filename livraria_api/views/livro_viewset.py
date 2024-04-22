from rest_framework import viewsets
from ..serializers import LivroSerializer
from ..models import Livro
from ..permissions import IsGetOrAuthenticated


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsGetOrAuthenticated]
