from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout


# Create your views here.
def index(request):
    return render(request,'menu/index.html')

def v_perfilusuario(request):
    return render(request, 'menu/v_perfilusuario.html')

def bandanas(request):
    return render(request,'menu/bandanas.html')

def h_RegistrarUsuario(request):
    return render(request,'menu/h_RegistrarUsuario.html')

def f_RegistroUsuario(request):
    nombre=request.POST["nombreUsuario"]
    correo=request.POST["correo"]
    contrasena=request.POST["contrasena"]
    pregunta=request.POST["preguntaSecreta"]
    respuesta=request.POST["respuesta"]   







    return render(request,'menu/f_RegistroUsuario.html')

def h_recuperarContrasena(request):
    return render(request,'menu/h_recuperarContrasena.html')

def f_recuperacionContrasena(request):
    return render(request,'menu/f_recuperacionContrasena.html')

def h_modificarContrasena(request):
    return render(request,'menu/h_modificarContrasena.html')

def f_modificacionContrasena(request):
    return render(request,'menu/f_modificacionContrasena.html')

def h_inicioSesion(request):
    return render(request,'menu/h_inicioSesion.html') 

def f_iniciarSesion(request):
    #esto es el ejemplo, debemos adaptarlo. se importaron 2 librerias.
    usuario1=request.POST['usuario']
    contrasena1=request.POST['contra']
    try:
        user1=User.objects.het(username=usuario1)
    except user.DoesNotExist:
        messages.error(request,'El usuario o la conrtraseña son incorrectas')
        return redirect('Iniciar')

    pass_valida = check_password(contra1,user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la conraseña son incorrectas')
        return redirect ('Iniciar')
    usuario2 = Usuario.objects.get(username = usuario1,constrasennia=contra1)
    user = authenticate(username=usuario1,password=contra1)
    if user is not None:
        login(request,user)
        if(usuario2.tipousuario.idTipoUsuario==1):
            return redirect ('menu_admin')
        else:
            contexto = {"usuario":usuario2}
    return render(request,'menu/f_iniciarSesion.html')

def collares(request):
    return render(request,'menu/collares.html')

def correas(request):
    return render(request,'menu/correas.html')

def publicidad(request):
    return render(request,'menu/publicidad.html')

def ApiNoticias (request):
    return render(request,'menu/ApiNoticias.html')

def carrodecompra(request):
    return render(request, 'menu/carrodecompra.html')

def bandana_GatoCeleste(request):
    return render(request,'menu/bandana_GatoCeleste.html')

def bandana_GatoCuadrille(request):
    return render(request,'menu/bandana_GatoCuadrille.html')

def bandana_GatoFifi(request):
    return render(request,'menu/bandana_GatoFifi.html')

def bandana_GatoLocura(request):
    return render(request,'menu/bandana_GatoLocura.html')

def bandana_GatoStreet(request):
    return render(request,'menu/bandana_GatoStreet.html')

def bandana_PerroCuadrille(request):
    return render(request,'menu/bandana_PerroCuadrille.html')

def bandana_PerroRayasLocas(request):
    return render(request,'menu/bandana_PerroRayasLocas.html')

def bandana_perroTrajeEleganteRojo(request):
    return render(request,'menu/bandana_perroTrajeEleganteRojo.html')

def bandana_perroTrajeEleganteDorado(request):
    return render(request,'menu/bandana_perroTrajeEleganteDorado.html')

def collar_GatoAzul(request):
    return render(request,'menu/collar_GatoAzul.html')

def collar_GatoCarreras(request):
    return render(request,'menu/collar_GatoCarreras.html')

def collar_gatoFreestyle(request):
    return render(request,'menu/collar_gatoFreestyle.html')

def collar_gatoValentin(request):
    return render(request,'menu/collar_gatoValentin.html')

def collar_gatoStreet(request):
    return render(request,'menu/collar_gatoStreet.html')

def collar_PerroBlanco(request):
    return render(request,'menu/collar_PerroBlanco.html')

def collar_PerroCafe(request):
    return render(request,'menu/collar_PerroCafe.html')

def collar_PerroRojo(request):
    return render(request,'menu/collar_PerroRojo.html')

def collar_PerroVainilla(request):
    return render(request,'menu/collar_PerroVainilla.html')

def correa_GatoAzul(request):
    return render(request,'menu/correa_GatoAzul.html')

def correa_GatoCuadrilles(request):
    return render(request,'menu/correa_GatoCuadrilles.html')

def correa_GatoFreestyle(request):
    return render(request,'menu/correa_GatoFreestyle.html')

def correa_GatoNegra(request):
    return render(request,'menu/correa_GatoNegra.html')

def correa_GatoRosada(request):
    return render(request,'menu/correa_GatoRosada.html')

def correa_PerroAzul(request):
    return render(request,'menu/correa_PerroAzul.html')

def cr_perronegra(request):
    return render(request,'menu/cr_perronegra.html')

def cr_perronegracadena(request):
    return render(request,'menu/cr_perronegracadena.html')

def correa_PerroRojo(request):
    return render(request,'menu/correa_PerroRojo.html')

def h_modificarAccesorios(request):
    return render(request, 'menu/h_modificarAccesorios.html')

def f_modificacionAccesorios(request):
    return render(request, 'menu/f_modificacionAccesorios.html')

def h_listarAccesorios(request):
    return render(request, 'menu/h_listarAccesorios.html')

def f_listadoAccesorios(request):
    return render(request, 'menu/f_listadoAccesorios.html')

def inicio_sesion_admin(request):
    return render(request, 'menu/inicio_sesion_admin.html')

def h_borrarAccesorios(request):
    return render(request, 'menu/h_borrarAccesorios.html')

def f_h_borrarAccesorios(request):
    return render(request, 'menu/f_h_borrarAccesorios.html')

def h_AgregarAccesorios(request):
    return render(request, 'menu/h_AgregarAccesorios.html')

def f_AgregagoAccesorios(request):
    return render(request, 'menu/f_AgregagoAccesorios.html')