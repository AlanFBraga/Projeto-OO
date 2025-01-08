# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def lista_livros(request):
    # Captura a pesquisa, se existir
    query = request.GET.get('q', '')
    if query:
        livros = Livro.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
    else:
        livros = Livro.objects.all()  # Lista todos os livros

    return render(request, 'livros/lista_livros.html', {'livros': livros, 'query': query})

@login_required
def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')  # Redireciona para a lista de livros
    else:
        form = LivroForm()

    return render(request, 'livros/criar_editar_livro.html', {'form': form, 'acao': 'Criar'})

@login_required
def editar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')  # Redireciona para a lista de livros
    else:
        form = LivroForm(instance=livro)

    return render(request, 'livros/criar_editar_livro.html', {'form': form, 'acao': 'Editar', 'livro': livro})

@login_required
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)

    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')  # Redireciona para a lista de livros

    return render(request, 'livros/excluir_livro.html', {'livro': livro})

