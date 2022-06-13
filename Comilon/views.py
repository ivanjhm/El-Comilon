from django.shortcuts import render, redirect
from django.contrib import messages
from Comilon.models import Rol, Usuario

# Create your views here.
def index6(request):
    return render(request,'comilon/index-6.html')

def inicio(request):
    return render(request,'comilon/login.html')


def register(request):
    return render(request,'comilon/register.html')

def registrando(request):
    email=request.POST['email']
    passw=request.POST['cont']
    rut=request.POST['rut']
    rol=request.POST['elrol']
    rol2=Rol.objects.get(id_Rol = rol)
    
    Usuario.objects.create(correo = email, clave = passw, rut = rut, rol=rol2)