#CRUD LISTAR E CADASTRAR
from django.shortcuts import render, redirect
from .models import Obra
from .forms import ObraForm

def login(request):
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