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
from .views import uno,dos,tres,cuatro,cinco,carrodecompra,api,InicioSesion,m_contraseña,r_contraseña,registrarusuario,v_perfilusuario
from .views import add_newaccesorios,inicio_sesion_admin,delete_accesorios,listar_accesorios,modify_accesorios
from .views import b_gatoceleste,b_gatocuadrille,b_gatofifi,b_gatolocura,b_gatostreet,b_perrocuadrille,b_perrorayaslocas,b_perrotrajelegante5,b_perrotrajelegante7
from .views import c_gatoazul,c_gatocarreras,c_gatofreestyle,c_gatosnvalentin,c_gatostreet,c_perroblanco,c_perrocafe,c_perrorojo,c_perrovainilla
from .views import cr_gatoazul,cr_gatocuadrilles,cr_gatofreestyle,cr_gatonegra,cr_gatorosada,cr_perroazul,cr_perronegra,cr_perronegracadena,cr_perrorojo

urlpatterns = [
    path('',uno,name="uno"),
    path('dos.html',dos,name="dos"),
    path('tres.html',tres,name="tres"),
    path('cuatro.html',cuatro,name="cuatro"),
    path('cinco.html',cinco,name="cinco"),
    path('carrodecompra.html',carrodecompra,name="carrodecompra"),
    path('api.html',api,name="api"),
    path('InicioSesion.html',InicioSesion,name="InicioSesion"),
    path('m_contraseña.html',m_contraseña,name="m_contraseña"),
    path('r_contraseña.html',r_contraseña,name="r_contraseña"),
    path('registrarusuario.html',registrarusuario,name="registrarusuario"),
    path('v_perfilusuario.html',v_perfilusuario,name="v_perfilusuario"),
    path('add_newaccesorios.html',add_newaccesorios,name="add_newaccesorios"),
    path('inicio_sesion_admin.html',inicio_sesion_admin,name="inicio_sesion_admin"),
    path('delete_accesorios.html',delete_accesorios,name="delete_accesorios"),
    path('listar_accesorios.html',listar_accesorios,name="listar_accesorios"),
    path('modify_accesorios.html',modify_accesorios,name="modify_accesorios"),
    path('b_gatoceleste.html',b_gatoceleste,name="b_gatoceleste"),
    path('b_gatocuadrille.html',b_gatocuadrille,name="b_gatocuadrille"),
    path('b_gatofifi.html',b_gatofifi,name="b_gatofifi"),
    path('b_gatolocura.html',b_gatolocura,name="b_gatolocura"),
    path('b_gatostreet.html',b_gatostreet,name="b_gatostreet"),
    path('b_perrocuadrille.html',b_perrocuadrille,name="b_perrocuadrille"),
    path('b_perrorayaslocas.html',b_perrorayaslocas,name="b_perrorayaslocas"),
    path('b_perrotrajelegante5.html',b_perrotrajelegante5,name="b_perrotrajelegante5"),
    path('b_perrotrajelegante7.html',b_perrotrajelegante7,name="b_perrotrajelegante7"),
    path('c_gatoazul.html',c_gatoazul,name="c_gatoazul"),
    path('c_gatocarreras.html',c_gatocarreras,name="c_gatocarreras"),
    path('c_gatofreestyle.html',c_gatofreestyle,name="c_gatofreestyle"),
    path('c_gatosnvalentin.html',c_gatosnvalentin,name="c_gatosnvalentin"),
    path('c_gatostreet.html',c_gatostreet,name="c_gatostreet"),
    path('c_perroblanco.html',c_perroblanco,name="c_perroblanco"),
    path('c_perrocafe.html',c_perrocafe,name="c_perrocafe"),
    path('c_perrorojo.html',c_perrorojo,name="c_perrorojo"),
    path('c_perrovainilla.html',c_perrovainilla,name="c_perrovainilla"),
    path('cr_gatoazul.html',cr_gatoazul,name="cr_gatoazul"),
    path('cr_gatocuadrilles.html',cr_gatocuadrilles,name="cr_gatocuadrilles"),
    path('cr_gatofreestyle.html',cr_gatofreestyle,name="cr_gatofreestyle"),
    path('cr_gatonegra.html',cr_gatonegra,name="cr_gatonegra"),
    path('cr_gatorosada.html',cr_gatorosada,name="cr_gatorosada"),
    path('cr_perroazul.html',cr_perroazul,name="cr_perroazul"),
    path('cr_perronegra.html',cr_perronegra,name="cr_perronegra"),
    path('cr_perronegracadena.html',cr_perronegracadena,name="cr_perronegracadena"),
    path('cr_perrorojo.html',cr_perrorojo,name="cr_perrorojo"),
]
