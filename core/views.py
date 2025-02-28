#CRUD LISTAR E CADASTRAR
from django.shortcuts import render, redirect
from .models import Obra
from .forms import ObraForm
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

def listar_obras(request):
    obras = Obra.objects.all()
    contexto={
        'todas_obras': obras
    }
    return render(request, 'home.html', contexto)

def cadastrar_obras(request):   
    form = ObraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_obras')
    
    contexto = {
        'form_obra': form
    }
    return render(request, 'obras_cadastrar.html', contexto)
