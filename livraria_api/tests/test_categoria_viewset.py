from rest_framework.test import APITestCase
from ..models import Categoria
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status


class CategoriaViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testeuser", password="testepassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.url_list = reverse('categoria-list')

    def test_listar_todas_as_categorias(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Categoria.objects.all().count())

    def test_criar_uma_nova_categoria(self):
        data = {"nome": "Autor", "ativo": True}
        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Categoria.objects.filter(nome="Autor").exists())

    def test_atualizar_uma_categoria(self):
        categoria = Categoria.objects.create(nome="Categoria", ativo=True)
        data = {"nome": "Nova Categoria"}
        response = self.client.put(
            reverse('categoria-detail', args=[categoria.id]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Categoria.objects.filter(
            nome="Nova Categoria").exists())

    def test_deletar_uma_categoria(self):
        categoria = Categoria.objects.create(nome="Categoria", ativo=True)
        response = self.client.delete(
            reverse('categoria-detail', args=[categoria.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Categoria.objects.filter(id=categoria.id).exists())
