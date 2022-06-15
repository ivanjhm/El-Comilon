from django.shortcuts import render, redirect
from django.contrib import messages
from Comilon.models import Rol, Usuario, Cliente

# Create your views here.
def index6(request):
    return render(request,'comilon/index-6.html')

def inicio(request):
    return render(request,'comilon/login.html')


def register(request):
    return render(request,'comilon/register.html')

def registrando(request):
    email=request.POST['correo']
    passw=request.POST['password1']
    rut=request.POST['rut']
    rol=request.POST['elrol']
    rol2=Rol.objects.get(id_Rol = rol)
    nombre=request.POST['nomb']
    apellido=request.POST['ap']

    if Usuario.objects.filter(correo=email).exists():
        messages.add_message(request=request, level=messages.SUCCESS, message="El correo esta registrado")
        return redirect('index-6')
    else:
        Usuario.objects.create(correo=email, clave=passw, rut=rut, rol=rol2)
        Cliente.objects.create(rut=rut, nombres=nombre, apellidos=apellido, correo=email)
        messages.add_message(request=request, level=messages.SUCCESS, message="has sido registrado correctamente")
        return redirect('index-6')
