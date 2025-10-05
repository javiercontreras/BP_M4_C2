from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def saludo_v2(request, nombre, apellido):
    context = {
    'nombre': nombre.capitalize(),
    'apellido': apellido.upper(),
    }
    return render(request, 'saludo_v2.html', context)