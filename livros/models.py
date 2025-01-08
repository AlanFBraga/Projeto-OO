# livros/models.py

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    isbn = models.CharField(max_length=13)
    resumo = models.TextField()
    categoria = models.ForeignKey(Categoria, related_name='livros', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
