from django.test import TestCase
from ..models import Categoria


class CategoriaTestCase(TestCase):
    def setUp(self):
        Categoria.objects.create(nome="Suspense", ativo=True)
        Categoria.objects.create(nome="Romance", ativo=False)

    def test_categoria_is_created(self):
        categoria = Categoria.objects.get(nome="Suspense")
        self.assertTrue(categoria.id is not None)

    def test_categoria_return_str(self):
        categoria = Categoria.objects.get(nome="Suspense")
        self.assertEqual(categoria.__str__(), "Suspense")

    def test_categoria_return_active(self):
        categoria = Categoria.objects.get(nome="Suspense")
        categoria_inativo = Categoria.objects.get(nome="Romance")
        self.assertEqual(categoria.ativo, True)
        self.assertEqual(categoria_inativo.ativo, False)
