from django.urls import reverse
from rest_framework import status
from ..models import Autor
from rest_framework.test import APITestCase
from datetime import date


class AutorViewSetTest(APITestCase):
    def setUp(self):
        self.url_list = reverse('livro-list')

    def test_listagem_de_autores(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Autor.objects.all().count())

    def test_criacao_de_novo_autor(self):
        data = {"nome": "AutorTeste2", "data_nascimento": date(
            1990, 1, 1), "ativo": True}

        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Autor.objects.filter(nome="AutorTeste2").exists())

    def test_atualizacao_de_autor(self):
        autor = Autor.objects.create(
            nome="AutorTeste2", data_nascimento=date(1990, 1, 1), ativo=True)
        data = {"nome": "AutorTeste34"}
        response = self.client.put(
            reverse('autor-detail', args=[autor.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        autor_atualizado = Autor.objects.filter(id=autor.id)
        self.assertEqual(autor_atualizado.nome, "AutorTeste34")

    def test_exclusao_de_autor(self):
        autor = Autor.objects.create(
            nome="AutorTeste2", data_nascimento=date(1990, 1, 1), ativo=True)
        response = self.client.delete(
            reverse('autor-detail', args=[autor.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Autor.objects.filter(id=autor.id).exists())
