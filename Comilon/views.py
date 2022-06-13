from django.shortcuts import render, redirect
from django.contrib import messages
from Comilon.models import Rol, Usuario, Cliente

# Create your views here.


def index6(request):
    return render(request, 'comilon/index-6.html')


def inicio(request):
    return render(request, 'comilon/login.html')


def register(request):
    return render(request, 'comilon/register.html')


def registrando(request):
    email = request.POST['correo']
    passw = request.POST['password1']
    passw2 = request.POST['password2']
    rut = request.POST['rut']
    rol = request.POST['elrol']
    rol2 = Rol.objects.get(id_Rol=rol)
    nombre = request.POST['nomb']
    apellido = request.POST['ap']

    if Usuario.objects.filter(correo=email).exists():
        messages.info(request, 'El correo esta registrado')
        return redirect('index-6')
    else:
        Usuario.objects.create(correo=email, clave=passw, rut=rut, rol=rol2)
        Cliente.objects.create(rut=rut, nombres=nombre, apellidos=apellido, correo=email)
        messages.info(request, 'Te has registrado en la plataforma')
        return redirect('index-6')
