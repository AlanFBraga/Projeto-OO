# livros/admin.py

from django.contrib import admin
from .models import Livro, Categoria

admin.site.register(Livro)
admin.site.register(Categoria)