# livros/forms.py

from django import forms
from .models import Livro, Categoria

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'data_publicacao', 'isbn', 'resumo', 'categoria']
