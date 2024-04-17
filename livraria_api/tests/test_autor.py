from django.test import TestCase
from datetime import date
from ..models import Autor


class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(
            nome="Joao", data_nascimento=date(1990, 1, 1), ativo=True)
        Autor.objects.create(
            nome="Maria", data_nascimento=date(1997, 1, 1), ativo=False)

    def test_criacao_do_autor(self):
        autor = Autor.objects.get(nome="Joao")
        self.assertTrue(autor.id is not None)

    def test_autor_return_str(self):
        autor = Autor.objects.get(nome="Joao")
        self.assertEqual(autor.__str__(), "Joao")

    def test_se_autor_estiver_ativo(self):
        autor_ativo = Autor.objects.get(nome="Joao")
        autor_inativo = Autor.objects.get(nome="Maria")
        self.assertTrue(autor_ativo.ativo)
        self.assertFalse(autor_inativo.ativo)

    def test_data_nascimento_do_autor(self):
        autor = Autor.objects.get(nome="Joao")
        self.assertEqual(autor.data_nascimento, date(1990, 1, 1))
