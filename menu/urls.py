"""
URL configuration for PetShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index,collares,bandanas,correas,publicidad,carrodecompra,api,h_inicioSesion,h_modificarContrasena,h_recuperarContrasena,h_RegistrarUsuario,v_perfilusuario
from .views import h_AgregarAccesorios,inicio_sesion_admin,borrar_Accesorios,h_listarAccesorios,h_modificarAccesorios
from .views import bandana_GatoCeleste,bandana_GatoCuadrille,bandana_GatoFifi,bandana_GatoLocura,bandana_GatoStreet,bandana_PerroCuadrille,bandana_PerroRayasLocas,bandana_perroTrajeEleganteRojo,bandana_perroTrajeEleganteDorado
from .views import collar_GatoAzul,collar_GatoCarreras,collar_gatoFreestyle,collar_gatoValentin,collar_gatoStreet,collar_PerroBlanco,collar_PerroCafe,collar_PerroRojo,collar_PerroVainilla
from .views import correa_GatoAzul,correa_GatoCuadrilles,correa_GatoFreestyle,correa_GatoNegra,correa_GatoRosada,correa_PerroAzul,cr_perronegra,cr_perronegracadena,correa_PerroRojo

urlpatterns = [
    path('',index,name="index"),
    path('collares.html',collares,name="collares"),
    path('bandanas.html',bandanas,name="bandanas"),
    path('correas.html',correas,name="correas"),
    path('publicidad.html',publicidad,name="publicidad"),
    path('carrodecompra.html',carrodecompra,name="carrodecompra"),
    path('api.html',api,name="api"),
    path('h_inicioSesion.html',h_inicioSesion,name="h_inicioSesion"),
    path('h_modificarContrasena.html',h_modificarContrasena,name="h_modificarContrasena"),
    path('h_recuperarContrasena.html',h_recuperarContrasena,name="h_recuperarContrasena"),
    path('h_RegistrarUsuario.html',h_RegistrarUsuario,name="h_RegistrarUsuario"),
    path('v_perfilusuario.html',v_perfilusuario,name="v_perfilusuario"),
    path('h_AgregarAccesorios.html',h_AgregarAccesorios,name="h_AgregarAccesorios"),
    path('inicio_sesion_admin.html',inicio_sesion_admin,name="inicio_sesion_admin"),
    path('borrar_Accesorios.html',borrar_Accesorios,name="borrar_Accesorios"),
    path('h_listarAccesorios.html',h_listarAccesorios,name="h_listarAccesorios"),
    path('h_modificarAccesorios.html',h_modificarAccesorios,name="h_modificarAccesorios"),
    path('bandana_GatoCeleste.html',bandana_GatoCeleste,name="bandana_GatoCeleste"),
    path('bandana_GatoCuadrille.html',bandana_GatoCuadrille,name="bandana_GatoCuadrille"),
    path('bandana_GatoFifi.html',bandana_GatoFifi,name="bandana_GatoFifi"),
    path('bandana_GatoLocura.html',bandana_GatoLocura,name="bandana_GatoLocura"),
    path('bandana_GatoStreet.html',bandana_GatoStreet,name="bandana_GatoStreet"),
    path('bandana_PerroCuadrille.html',bandana_PerroCuadrille,name="bandana_PerroCuadrille"),
    path('bandana_PerroRayasLocas.html',bandana_PerroRayasLocas,name="bandana_PerroRayasLocas"),
    path('bandana_perroTrajeEleganteRojo.html',bandana_perroTrajeEleganteRojo,name="bandana_perroTrajeEleganteRojo"),
    path('bandana_perroTrajeEleganteDorado.html',bandana_perroTrajeEleganteDorado,name="bandana_perroTrajeEleganteDorado"),
    path('collar_GatoAzul.html',collar_GatoAzul,name="collar_GatoAzul"),
    path('collar_GatoCarreras.html',collar_GatoCarreras,name="collar_GatoCarreras"),
    path('collar_gatoFreestyle.html',collar_gatoFreestyle,name="collar_gatoFreestyle"),
    path('collar_gatoValentin.html',collar_gatoValentin,name="collar_gatoValentin"),
    path('collar_gatoStreet.html',collar_gatoStreet,name="collar_gatoStreet"),
    path('collar_PerroBlanco.html',collar_PerroBlanco,name="collar_PerroBlanco"),
    path('collar_PerroCafe.html',collar_PerroCafe,name="collar_PerroCafe"),
    path('collar_PerroRojo.html',collar_PerroRojo,name="collar_PerroRojo"),
    path('collar_PerroVainilla.html',collar_PerroVainilla,name="collar_PerroVainilla"),
    path('correa_GatoAzul.html',correa_GatoAzul,name="correa_GatoAzul"),
    path('correa_GatoCuadrilles.html',correa_GatoCuadrilles,name="correa_GatoCuadrilles"),
    path('correa_GatoFreestyle.html',correa_GatoFreestyle,name="correa_GatoFreestyle"),
    path('correa_GatoNegra.html',correa_GatoNegra,name="correa_GatoNegra"),
    path('correa_GatoRosada.html',correa_GatoRosada,name="correa_GatoRosada"),
    path('correa_PerroAzul.html',correa_PerroAzul,name="correa_PerroAzul"),
    path('cr_perronegra.html',cr_perronegra,name="cr_perronegra"),
    path('cr_perronegracadena.html',cr_perronegracadena,name="cr_perronegracadena"),
    path('correa_PerroRojo.html',correa_PerroRojo,name="correa_PerroRojo"),
]
