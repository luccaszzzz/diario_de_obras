from django.db import models

class Obra(models.Model):
    titulo  = models.CharField(max_length=100)
    descricao = models.TextField()
    data_obra = models.DateField()


