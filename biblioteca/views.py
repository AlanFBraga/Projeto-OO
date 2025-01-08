# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário
            return redirect('login')  # Redireciona para a página de login após criar a conta
    else:
        form = UserCreationForm()  # Exibe o formulário vazio

    return render(request, 'signup.html', {'form': form})

# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redireciona para a home após o login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
