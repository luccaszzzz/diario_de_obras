from django.shortcuts import render, redirect, get_object_or_404
from .models import Obra
from .forms import ObraForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect("listar_obras")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, "login.html")


def listar_obras(request):
    obras = Obra.objects.all()
    contexto = {"todas_obras": obras}
    return render(request, "obras_listar.html", contexto)


def cadastrar_obras(request):
    form = ObraForm(
        request.POST or None, request.FILES or None
    )  # Adiciona request.FILES para receber arquivos
    if form.is_valid():
        form.save()
        return redirect("listar_obras")
    contexto = {"form_obra": form}
    return render(request, "obras_cadastrar.html", contexto)


def editar_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    if request.method == "POST":
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect("listar_obras")
    else:
        form = ObraForm(instance=obra)
    contexto = {"form_obra": form}
    return render(request, "obras_editar.html", contexto)


def excluir_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    if request.method == "POST":
        obra.delete()
        return redirect("listar_obras")
    contexto = {"obra": obra}
    return render(request, "obras_excluir.html", contexto)


def revisar_obra(request, id):
    obra = get_object_or_404(Obra, id=id)
    contexto = {"obra": obra}
    return render(request, "obras_revisar.html", contexto)



'''
============= OBRA API =============
'''

@api_view(['GET'])
def obraAPIlistar(request):
    obras = Obra.objects.all()
    obra_serializer = ObraSerializer(obras, many=True)
    return Response(obra_serializer.data)

@api_view(['PUT'])
def obraAPIadicionar(request):
    obra = ObraSerializer(data=request.data)
    if obra.is_valid():
        obra.save()
        return Response(obra.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def obraAPIatualizar(request, id):
    obra_bd = Obra.objects.get(id=id)
    obra = ObraSerializer(data=request.data,
                                 instance=obra_bd)
    if obra.is_valid():
        obra.save()
        return Response(obra.data, status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def obraAPIremover(request, id):
    obra_bd = Obra.objects.get(id=id)
    if obra_bd:
        obra_bd.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)