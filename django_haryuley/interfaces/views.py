from django.shortcuts import render
#from django.http import HttpResponse


def inicio(request):
    return render(request,'Inicio.html')

def acerca(request):
    return render (request,'acerca.html')
