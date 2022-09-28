from venv import create
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def Registro(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        nombre =request.POST['nombre']
        apellido =request.POST['apellido']
        email = request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']

        myuser = User.objects.create_user( usuario, email, pass1)
        myuser.nombre_user = nombre
        myuser.apellido_user = apellido

        myuser.save()

        messages.success(request, "Verifica tu cuenta")

        return redirect("login")

    return render(request,'CuentaUsuario/Registro.html')

def Usuario(request):

    if request.method == 'POST':
        usuario = request.POST['usuario']
        pass1 = request.POST['pass1']

        user = authenticate(usuario=usuario, pass1=pass1)

        if user is not None:
            login(request, user)
            usuario1 =  user.nombre_user
            return render(request, 'CuentaUsuario/usuario.html', {'usuario': usuario1})
        else:
            messages.error(request, "Datos incorrectos")
            return redirect ('inicio')
    
    return render(request, 'CuentaUsuario/login.html')


def inicio(request):
    return render(request,'interfaces_inicio/Inicio.html')

def acerca(request):
    return render (request,'interfaces_inicio/acerca.html')

def productos(request):
    return render(request,'interfaces_inicio/productos.html')

def contacto(request):
    return render(request,'interfaces_inicio/contacto.html')

def login(request):
    return render(request,'CuentaUsuario/login.html')

def Oferta(request):
    return render(request,'interfaces_inicio/Oferta.html')

def usuario(request):
    return render(request, 'CuentaUsuario/usuario.html')

