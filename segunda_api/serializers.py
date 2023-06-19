from rest_framework import serializers
from menu.models import Preguntas
class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields =['ID_Preguntas','pregunta']