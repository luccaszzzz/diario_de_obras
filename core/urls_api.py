from django.urls import path
from .views import *

urlpatterns = [

    # OBRAS API URL
    path('obras/listar/', obraAPIlistar),
    path('obras/adicionar/', obraAPIadicionar),
    path('obras/atualizar/<int:id>/', obraAPIatualizar),
    path('obras/remover/<int:id>/', obraAPIremover),
    
]