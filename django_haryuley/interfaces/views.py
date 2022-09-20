from contextlib import redirect_stderr
from django.shortcuts import render
#from django.http import HttpResponse


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

def Registro(request):
    return render(request,'CuentaUsuario/Registro.html')

def Oferta(request):
    return render(request,'interfaces_inicio/Oferta.html')

