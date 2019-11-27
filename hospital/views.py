import datetime
from django.template import loader
from django.shortcuts import render

def login(request):
    return render(request,"login.html")

def index(request):
    user = "Rodrigo Richards"
    tipo = "Administrador"
    return render(request,"index.html",{"usuario":user,"tipousuario":tipo})

def crearFicha(request):
    tipo = "Administrador"
    user = "Rodrigo Richards"
    return render(request,"crearFicha.html",{"usuario":user,"tipousuario":tipo})