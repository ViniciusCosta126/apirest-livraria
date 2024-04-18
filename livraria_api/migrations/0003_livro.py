# Generated by Django 5.0.4 on 2024-04-17 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria_api', '0002_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantidade', models.IntegerField(blank=True, default=0, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('data_lancamento', models.DateField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livraria_api.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livraria_api.categoria')),
            ],
        ),
    ]