from django.urls import path
from api_noticias.views import lista_usuarios

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
]