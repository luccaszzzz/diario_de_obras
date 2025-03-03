from django import forms
from .models import Obra


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ["titulo", "descricao", "data_obra"]
        widgets = {
            'data_obra': forms.DateInput(attrs={'type': 'date'})  # Aqui você define o tipo como 'date' para ativar o calendário
        }