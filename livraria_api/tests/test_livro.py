from django.test import TestCase
from ..models import Autor, Categoria, Livro
from datetime import date


class LivroTestCase(TestCase):
    def setUp(self):
        autor = Autor.objects.create(
            nome="Joao", data_nascimento=date(1990, 1, 1), ativo=True)
        categoria = Categoria.objects.create(nome="Suspense", ativo=True)
        Livro.objects.create(
            titulo="Teste", descricao="Teste de livro de descricao", preco=29.99, quantidade=10, ativo=True,
            data_lancamento=date(2012, 1, 1), autor=autor, categoria=categoria)

    def test_livro_is_created(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertTrue(livro.id is not None)

    def test_livro_retorna_titulo_de_forma_correta(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.titulo, "Teste")

    def test_livro_retorna_descricao_de_forma_correta(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.descricao, "Teste de livro de descricao")

    def test_livro_retorna_preco_de_forma_correta(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(float(livro.preco), 29.99)

    def test_livro_retorna_quantidade_de_forma_correta(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.quantidade, 10)

    def test_livro_retorna_data_lancamento_de_forma_correta(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.data_lancamento, date(2012, 1, 1))

    def test_livro_retorna_autor_de_forma_correta(self):
        autor = Autor.objects.get(nome="Joao")
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.autor, autor)

    def test_livro_retorna_categoria_de_forma_correta(self):
        categoria = Categoria.objects.get(nome="Suspense")
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.categoria, categoria)

    def test_livro_retorna_ativo_de_forma_correta(self):
        livro = Livro.objects.get(titulo="Teste")
        self.assertEqual(livro.ativo, True)
