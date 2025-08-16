from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cursos(request):
    return render(request, 'cursos.html')

def registro(request):
    return render(request, 'registro.html')

def administracion(request):
    return render(request, 'administracion.html')
