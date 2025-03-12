from django.db import models
from django import forms


class Obra(models.Model):
    STATUS_CHOICES = [
        ("nao-iniciada", "Não Iniciada"),
        ("em-andamento", "Em Andamento"),
        ("concluida", "Concluída"),
        ("paralisada", "Paralisada"),
    ]

    titulo = models.CharField(max_length=200)
    data_obra = models.DateField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="imagens/", blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="nao-iniciada"
    )

    def __str__(self):
        return self.titulo


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ["titulo", "data_obra", "descricao", "imagem", "status"]
