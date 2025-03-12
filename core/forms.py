from django import forms
from .models import Obra


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ["titulo", "descricao", "data_obra", "imagem", "status"]
        widgets = {
            "data_obra": forms.DateInput(
                attrs={"type": "date"}
            ),  # Define o tipo como 'date' para ativar o calendário
            "status": forms.Select(
                choices=[
                    ("nao-iniciada", "Não Iniciada"),
                    ("em-andamento", "Em Andamento"),
                    ("concluida", "Concluída"),
                    ("paralisada", "Paralisada"),
                ]
            ),
        }

    imagem = forms.ImageField(required=False)  # Campo para upload de imagem
