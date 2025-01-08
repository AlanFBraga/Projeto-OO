
# Biblioteca Django

Olá! Esse projeto é uma aplicação web desenvolvida por mim com Django, com o objetivo de criar uma biblioteca digital onde é possível gerenciar livros de forma simples e eficiente. Você poderá listar os livros cadastrados, adicionar novos livros, editar ou excluir livros existentes, além de visualizar detalhes de cada um deles.

## Funcionalidades do Projeto

- **Listar Livros**: Exibe todos os livros cadastrados, com a possibilidade de buscar por título ou autor.
- **Adicionar Livro**: Permite o cadastro de novos livros com informações como título, autor, descrição e categoria.
- **Editar Livro**: Facilita a edição de qualquer livro já cadastrado.
- **Excluir Livro**: Exclui livros da biblioteca.
- **Detalhes do Livro**: Mostra mais informações detalhadas sobre cada livro.

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Django**: Framework web utilizado para criar toda a estrutura da aplicação.
- **Python**: Linguagem de programação principal.
- **SQLite**: Banco de dados utilizado por padrão no Django (pode ser substituído por outros, como MySQL ou PostgreSQL).
- **HTML/CSS**: Para estruturar e estilizar a interface da aplicação.

## Como Rodar o Projeto

Aqui estão os passos que você precisa seguir para rodar a aplicação localmente na sua máquina:

### 1. Clonando o Repositório

Primeiro, faça o clone deste repositório para sua máquina:

```bash
git clone https://github.com/seu-usuario/biblioteca-django.git
```

### 2. Instalando as Dependências

Navegue até o diretório do projeto:

```bash
cd biblioteca-django
```

Crie e ative um ambiente virtual (isso ajuda a manter o projeto isolado de outras configurações de Python na sua máquina):

- **No Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

- **No Mac/Linux**:

```bash
python3 -m venv venv
source venv/bin/activate
```

Depois de ativar o ambiente virtual, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### 3. Configurando o Banco de Dados

Agora, precisamos rodar as migrações para criar as tabelas no banco de dados:

```bash
python manage.py migrate
```

Se você for usar o banco de dados SQLite (que é o padrão), isso já deve estar pronto.

### 4. Criando um Superusuário

Para acessar a área de administração do Django e gerenciar os livros de maneira mais fácil, crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para criar o superusuário. Isso permitirá que você faça login na interface de administração e adicione, edite ou exclua livros.

### 5. Rodando o Servidor

Agora que tudo está pronto, você pode rodar o servidor de desenvolvimento para testar a aplicação:

```bash
python manage.py runserver
```

O Django vai rodar o servidor localmente e você pode acessar a aplicação no navegador em `http://127.0.0.1:8000/`.

### 6. Acessando o Painel de Administração

Se você quiser acessar a área administrativa, onde pode gerenciar os livros, acesse `http://127.0.0.1:8000/admin/` e faça login com o superusuário que você criou.

## Como Funciona

A aplicação exibe uma lista de livros onde você pode pesquisar por título ou autor. Ao clicar em um livro, você verá mais detalhes sobre ele. Você pode adicionar novos livros, editar os existentes e excluir livros que não são mais necessários.

### Páginas Importantes:

- **Lista de Livros**: A página inicial que mostra todos os livros cadastrados. Aqui você pode buscar por título ou autor, ou acessar as opções de adicionar, editar e excluir livros.
- **Detalhes do Livro**: Ao clicar em um livro, você verá suas informações completas.
- **Painel de Administração**: Se você for o administrador, pode adicionar, editar ou excluir livros diretamente pelo painel de administração do Django.
