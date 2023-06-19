from rest_framework import serializers
from menu.models import Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['ID_Usuario','Rut','Nombre','Apellido','Correo','Num_Celular','Clave','rol','preguntas','Respuesta']
        