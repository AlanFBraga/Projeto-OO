# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'),  # Página com a lista de livros
    path('criar/', views.criar_livro, name='criar_livro'),  # Adicionar livro
    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),  # Editar livro
    path('excluir/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),  # Excluir livro
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
