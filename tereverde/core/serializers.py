from rest_framework import serializers
from .models import Parque

class ParqueSerializer(serializers.ModelSerializer):
    
    nome_display = serializers.CharField(source='get_nome_display')

    class Meta:
        model = Parque
        fields = (
            'id', 
            'nome', 
            'nome_display',
            'descricao_geral', 
            'altitude_media', 
            'horario_funcionamento',
        )