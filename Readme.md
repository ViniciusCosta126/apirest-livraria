# Livraria - Api Rest

### Rodando localmente

- Clone o repositorio

```bash
git clone https://github.com/ViniciusCosta126/apirest-livraria.git
```

- Crie uma virutalenv

```bash
python -m venv env
```

- Ative a virtualenv

```bash
.\env\Scripts\activate
```

- Instale as dependencias

```bash
pip install -r requirements.txt
```

### Testes

- Para rodar os testes, rode o comando a seguir (Lembre que a virtualenv deve estar ativa), o argumento verbosity pode ir de 0 a 3, quanto maior o numero maior a especifidade

```bash
python manage.py test --verbosity=2
```
