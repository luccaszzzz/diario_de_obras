from django.forms import ModelForm
from .models import Obra

class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'descricao', 'data_obra']