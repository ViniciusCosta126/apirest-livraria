from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento = models.DateField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
