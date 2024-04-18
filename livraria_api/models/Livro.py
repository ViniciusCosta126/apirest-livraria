from django.db import models
from .Categoria import Categoria
from .Autor import Autor


class Livro(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    data_lancamento = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
