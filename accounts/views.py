from django.contrib.auth.views import LoginView
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'login.html'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz o login do usuário imediatamente após o cadastro
            return redirect('/')  # Redireciona para a página inicial após o login
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
