from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Faz login do usuário
            
            if user.is_superuser:  # Verifica se é um administrador
                auth_login(request, user)  # Faz login do usuário
                return redirect('home')  # Redireciona para a página inicial do sistema
        
        else:
            messages.error(request, "Usuário ou senha inválidos.")  # Mensagem de erro

    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')