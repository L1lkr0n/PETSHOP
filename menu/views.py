from django.shortcuts import render

# Create your views here.
def uno(request):
    return render(request,'menu/uno.html')

def v_perfilusuario(request):
    return render(request, 'menu/v_perfilusuario.html')

def tres(request):
    return render(request,'menu/tres.html')

def registrarusuario(request):
    return render(request,'menu/registrarusuario.html')

def registroUsuario(request):
    nombreU = request.POST['v_nombre']
    correoU = request.POST['v_gmail']
    contraU = request.POST['v_contraseña']
    preguntaS = request.POST['v_pregunta']
    respuestaU = request.POST['v_respuesta']
    

def r_contraseña(request):
    return render(request,'menu/r_contraseña.html')

def m_contraseña(request):
    return render(request,'menu/m_contraseña.html')

def InicioSesion(request):
    return render(request,'menu/InicioSesion.html')

def dos(request):
    return render(request,'menu/dos.html')

def cuatro(request):
    return render(request,'menu/cuatro.html')

def cinco(request):
    return render(request,'menu/cinco.html')

def api(request):
    return render(request,'menu/api.html')

def carrodecompra(request):
    return render(request, 'menu/carrodecompra.html')

def b_gatoceleste(request):
    return render(request,'menu/b_gatoceleste.html')

def b_gatocuadrille(request):
    return render(request,'menu/b_gatocuadrille.html')

def b_gatofifi(request):
    return render(request,'menu/b_gatofifi.html')

def b_gatolocura(request):
    return render(request,'menu/b_gatolocura.html')

def b_gatostreet(request):
    return render(request,'menu/b_gatostreet.html')

def b_perrocuadrille(request):
    return render(request,'menu/b_perrocuadrille.html')

def b_perrorayaslocas(request):
    return render(request,'menu/b_perrorayaslocas.html')

def b_perrotrajelegante5(request):
    return render(request,'menu/b_perrotrajelegante5.html')

def b_perrotrajelegante7(request):
    return render(request,'menu/b_perrotrajelegante7.html')

def c_gatoazul(request):
    return render(request,'menu/c_gatoazul.html')

def c_gatocarreras(request):
    return render(request,'menu/c_gatocarreras.html')

def c_gatofreestyle(request):
    return render(request,'menu/c_gatofreestyle.html')

def c_gatosnvalentin(request):
    return render(request,'menu/c_gatosnvalentin.html')

def c_gatostreet(request):
    return render(request,'menu/c_gatostreet.html')

def c_perroblanco(request):
    return render(request,'menu/c_perroblanco.html')

def c_perrocafe(request):
    return render(request,'menu/c_perrocafe.html')

def c_perrorojo(request):
    return render(request,'menu/c_perrorojo.html')

def c_perrovainilla(request):
    return render(request,'menu/c_perrovainilla.html')

def cr_gatoazul(request):
    return render(request,'menu/cr_gatoazul.html')

def cr_gatocuadrilles(request):
    return render(request,'menu/cr_gatocuadrilles.html')

def cr_gatofreestyle(request):
    return render(request,'menu/cr_gatofreestyle.html')

def cr_gatonegra(request):
    return render(request,'menu/cr_gatonegra.html')

def cr_gatorosada(request):
    return render(request,'menu/cr_gatorosada.html')

def cr_perroazul(request):
    return render(request,'menu/cr_perroazul.html')

def cr_perronegra(request):
    return render(request,'menu/cr_perronegra.html')

def cr_perronegracadena(request):
    return render(request,'menu/cr_perronegracadena.html')

def cr_perrorojo(request):
    return render(request,'menu/cr_perrorojo.html')

def modify_accesorios(request):
    return render(request, 'menu/modify_accesorios.html')

def listar_accesorios(request):
    return render(request, 'menu/listar_accesorios.html')

def inicio_sesion_admin(request):
    return render(request, 'menu/inicio_sesion_admin.html')

def delete_accesorios(request):
    return render(request, 'menu/delete_accesorios.html')

def add_newaccesorios(request):
    return render(request, 'menu/add_newaccesorios.html')