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
    path('dos',dos,name="dos"),
    path('tres',tres,name="tres"),
    path('cuatro',cuatro,name="cuatro"),
    path('cinco',cinco,name="cinco"),
    path('carrodecompra',carrodecompra,name="carrodecompra"),
    path('api',api,name="api"),
    path('InicioSesion',InicioSesion,name="InicioSesion"),
    path('m_contraseña',m_contraseña,name="m_contraseña"),
    path('r_contraseña',r_contraseña,name="r_contraseña"),
    path('registrarusuario',registrarusuario,name="registrarusuario"),
    path('v_perfilusuario',v_perfilusuario,name="v_perfilusuario"),
    path('add_newaccesorios',add_newaccesorios,name="add_newaccesorios"),
    path('inicio_sesion_admin',inicio_sesion_admin,name="inicio_sesion_admin"),
    path('delete_accesorios',delete_accesorios,name="delete_accesorios"),
    path('listar_accesorios',listar_accesorios,name="listar_accesorios"),
    path('modify_accesorios',modify_accesorios,name="modify_accesorios"),
    path('b_gatoceleste',b_gatoceleste,name="b_gatoceleste.html"),
    path('b_gatocuadrille',b_gatocuadrille,name="b_gatocuadrille.html"),
    path('b_gatofifi',b_gatofifi,name="b_gatofifi.html"),
    path('b_gatolocura',b_gatolocura,name="b_gatolocura.html"),
    path('b_gatostreet',b_gatostreet,name="b_gatostreet.html"),
    path('b_perrocuadrille',b_perrocuadrille,name="b_perrocuadrille.html"),
    path('b_perrorayaslocas',b_perrorayaslocas,name="b_perrorayaslocas.html"),
    path('b_perrotrajelegante5',b_perrotrajelegante5,name="b_perrotrajelegante5.html"),
    path('b_perrotrajelegante7',b_perrotrajelegante7,name="b_perrotrajelegante7.html"),
    path('c_gatoazul',c_gatoazul,name="c_gatoazul.html"),
    path('c_gatocarreras',c_gatocarreras,name="c_gatocarreras.html"),
    path('c_gatofreestyle',c_gatofreestyle,name="c_gatofreestyle.html"),
    path('c_gatosnvalentin',c_gatosnvalentin,name="c_gatosnvalentin.html"),
    path('c_gatostreet',c_gatostreet,name="c_gatostreet.html"),
    path('c_perroblanco',c_perroblanco,name="c_perroblanco.html"),
    path('c_perrocafe',c_perrocafe,name="c_perrocafe.html"),
    path('c_perrorojo',c_perrorojo,name="c_perrorojo.html"),
    path('c_perrovainilla',c_perrovainilla,name="c_perrovainilla.html"),
    path('cr_gatoazul',cr_gatoazul,name="cr_gatoazul"),
    path('cr_gatocuadrilles',cr_gatocuadrilles,name="cr_gatocuadrilles"),
    path('cr_gatofreestyle',cr_gatofreestyle,name="cr_gatofreestyle"),
    path('cr_gatonegra',cr_gatonegra,name="cr_gatonegra"),
    path('cr_gatorosada',cr_gatorosada,name="cr_gatorosada"),
    path('cr_perroazul',cr_perroazul,name="cr_perroazul"),
    path('cr_perronegra',cr_perronegra,name="cr_perronegra"),
    path('cr_perronegracadena',cr_perronegracadena,name="cr_perronegracadena"),
    path('cr_perrorojo',cr_perrorojo,name="cr_perrorojo"),
]
