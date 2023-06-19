from django.urls import path
from segunda_api.views import lista_preguntas

urlpatterns = [
    path('lista_preguntas', lista_preguntas, name="lista_preguntas"),
]