from rest_framework import serializers
from menu.models import Preguntas
class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields =['ID_Preguntas','pregunta']