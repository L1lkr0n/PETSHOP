from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages


# Create your views here.

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request,'menu/index.html')
@login_required(login_url='/h_inicioSesion')
def v_perfilusuario(request,pk):
   
    usuario=Usuario.objects.get(ID_Usuario=pk)
    contexto={
        "usuario":usuario
    }
    return render(request, 'menu/v_perfilusuario.html',contexto)

def bandanas(request):
    return render(request,'menu/bandanas.html')

def h_RegistrarUsuario(request):
    preguntas = Preguntas.objects.all()
    contexto = {
        "preg": preguntas
    }
    return render(request,'menu/h_RegistrarUsuario.html',contexto)

def f_RegistroUsuario(request):
    print("1")
    nombre=request.POST["nombreUsuario"]
    apellido=request.POST["apellidoUsuario"]
    correo=request.POST["correo"]
    contrasena=request.POST["contrasena"]
    pregunta=request.POST["preguntaSecreta"]
    respuesta=request.POST["respuesta"]
    rut=request.POST["rutUsuario"]
    numerocelular=request.POST["numCelularUsuario"]
    correoelectronico=request.POST["correo"]
    print("2")

    registroPregunta = Preguntas.objects.get(ID_Preguntas = pregunta)
    registrorol = Rol.objects.get(ID_Rol = 1)
    print("3")
    Usuario.objects.create(Rut = rut, Nombre =  nombre,Apellido = apellido, Num_Celular=numerocelular, Correo=correoelectronico ,Clave=contrasena ,preguntas = registroPregunta , Respuesta=respuesta, rol = registrorol)
    user = User.objects.create_user(username = correo, email = correo, password = contrasena)
    user.is_active = True
    user.save()
    print("4")
    messages.success(request, "Usuario Registrado Correctamente")
    return redirect('h_RegistrarUsuario')

def h_recuperarContrasena(request):
    preguntas = Preguntas.objects.all()
    contexto = {
        "preg": preguntas
    }
    return render(request,'menu/h_recuperarContrasena.html',contexto)

def f_recuperacionContrasena(request):
    correo=request.POST["correorecuperar"]
    respuesta=request.POST["respuestarecuperar"]
    preguntaS=request.POST["preguntasecreta"]

    recu = Usuario.objects.get(Correo = correo,Respuesta=respuesta,preguntas=preguntaS)
    if  recu is not None:
        if(recu.rol.ID_Rol==1 and recu.Correo==correo and recu.Respuesta==respuesta and recu.preguntas==preguntaS):
            return redirect ('h_modificarContrasena')
        else:
            return redirect ('h_recuperarContrasena')
    else:
        messages.error(request,'El usuario no existe')
    
    return render(request,'menu/f_recuperacionContrasena.html')

def h_modificarContrasena(request):
    return render(request,'menu/h_modificarContrasena.html')

def f_modificacionContrasena(request):
    correo = request.POST['correomodificar']





    return render(request,'menu/f_modificacionContrasena.html')

def h_inicioSesion(request):
    return render(request,'menu/h_inicioSesion.html') 

def f_iniciarSesion(request):
    #esto es el ejemplo, debemos adaptarlo. se importaron 2 librerias.
    usuario1=request.POST['usuario']
    contrasena1=request.POST['contra']
    try:
        user1= User.objects.get(username=usuario1)
    except User.DoesNotExist:
        messages.error(request,'El usuario o la contraseña son incorrectas')
        return redirect('h_inicioSesion')

    pass_valida = check_password(contrasena1,user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectas')
        return redirect ('h_inicioSesion')
    usuario2 = Usuario.objects.get(Correo = usuario1,Clave=contrasena1)
    user = authenticate(username=usuario1,password=contrasena1)
    if user is not None:
        login(request,user)
        if(usuario2.rol.ID_Rol==2):
            request.session['usuario'] = user1.username
            return redirect ('h_AgregarAccesorios')
        else:
            request.session['usuario'] = user1.username
            return redirect ('index')
    else:
        messages.error(request,'El usuario no existe')
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


@login_required(login_url='/h_inicioSesion')
def h_modificarAccesorios(request):
    return render(request, 'menu/h_modificarAccesorios.html')

def f_modificacionAccesorios(request):
    return render(request, 'menu/f_modificacionAccesorios.html')

@login_required(login_url='/h_inicioSesion')
def h_listarAccesorios(request):
    return render(request, 'menu/h_listarAccesorios.html')

def f_listadoAccesorios(request):
    return render(request, 'menu/f_listadoAccesorios.html')

def inicio_sesion_admin(request):
    return render(request, 'menu/inicio_sesion_admin.html')

@login_required(login_url='/h_inicioSesion')
def h_borrarAccesorios(request):
    return render(request, 'menu/h_borrarAccesorios.html')

def f_h_borrarAccesorios(request):
    return render(request, 'menu/f_h_borrarAccesorios.html')

@login_required(login_url='/h_inicioSesion')
def h_AgregarAccesorios(request):
    return render(request, 'menu/h_AgregarAccesorios.html')

def f_AgregagoAccesorios(request):
    return render(request, 'menu/f_AgregagoAccesorios.html')