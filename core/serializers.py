from rest_framework import serializers
from .models import Obra

class ObraSerializer(serializers.ModelSerializer):
    imagem = serializers.SerializerMethodField()  # Adiciona um campo customizado para a URL da imagem

    class Meta:
        model = Obra
        fields = ["id", "titulo", "descricao", "data_obra", "status", "imagem"]  # Inclua "id" e "imagem"

    def get_imagem(self, obj):
        request = self.context.get("request")
        if obj.imagem:
            return request.build_absolute_uri(obj.imagem.url)  # Retorna a URL completa
        return None
