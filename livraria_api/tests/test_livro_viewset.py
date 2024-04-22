from ..models import Livro, Categoria, Autor
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from datetime import date


class LivroViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testeuser", password="testepassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        self.url_list = reverse('livro-list')

    def test_listagem_de_todos_os_livros(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data), Livro.objects.all().count())

    def test_criacao_de_um_novo_livro(self):
        autor = Autor.objects.create(
            nome="AutorTeste2", data_nascimento=date(1990, 1, 1), ativo=True)
        categoria = Categoria.objects.create(
            nome="CategoriaTeste2", ativo=True)

        data = {
            "categoria": categoria.id,
            "autor": autor.id,
            "titulo": "Dom Casmurro3213123",
            "descricao": "12312312",
            "preco": 29.00,
            "quantidade": 10,
            "ativo": True,
            "data_lancamento": date(1990, 10, 10)
        }

        response = self.client.post(self.url_list, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Livro.objects.filter(
            titulo="Dom Casmurro3213123").exists())

    def test_atualizar_livro(self):
        livro = Livro.objects.create(
            titulo='Livro Existente',
            descricao='Descrição do livro existente',
            preco=29.99,
            quantidade=10,
            ativo=True,
            data_lancamento='2024-04-17',
            autor=Autor.objects.create(
                nome='João', data_nascimento='1990-01-01'),
            categoria=Categoria.objects.create(nome='Ficção')
        )
        data = {'titulo': 'Livro Atualizado'}
        url_detail = reverse('livro-detail', args=[livro.id])
        response = self.client.put(url_detail, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        livro_atualizado = Livro.objects.get(id=livro.id)
        self.assertEqual(livro_atualizado.titulo, 'Livro Atualizado')

    def test_deletar_livro(self):
        livro = Livro.objects.create(
            titulo='Livro a Ser Deletado',
            descricao='Descrição do livro a ser deletado',
            preco=19.99,
            quantidade=5,
            ativo=True,
            data_lancamento='2024-04-18',
            autor=Autor.objects.create(
                nome='Maria', data_nascimento='1980-05-10'),
            categoria=Categoria.objects.create(nome='Romance')
        )
        url_detail = reverse('livro-detail', args=[livro.id])
        response = self.client.delete(url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Livro.objects.filter(id=livro.id).exists())
