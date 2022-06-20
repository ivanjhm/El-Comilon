<<<<<<< Updated upstream
from django.shortcuts import render, redirect
from .models import Usuario, Rol, Cliente
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.




def index6(request):
    return render(request,'comilon/index-6.html')

def inicio(request):
    return render(request,'comilon/login.html')

def registro(request):
    return render(request,'comilon/register.html')

def user(request):
    return render(request,'comilon/indexUser.html')

def admin(request):
    return render(request,'comilon/index.html')

def menu(request):
    return render(request,'comilon/grid-listing-masonry.html')

def plato (request):
    return render(request,'comilon/detail-restaurant.html')


def inicio_sesion(request):
    cor = request.POST['email']
    cont = request.POST['password']


    try:
        x = Usuario.objects.get(correo = cor, clave = cont)
        rol2 = Rol.objects.get(nombre = "Cliente")

        if x.rol == rol2:
            cli= Cliente.objects.get(rut = x.rut)
            contexto ={"Cliente": x, "datos": cli}

            return render(request,'comilon/indexUser.html',contexto)

        else:
            contexto ={"Administrador": x}
            return render(request,'comilon/index.html',contexto)
    except Usuario.DoesNotExist:
        messages.add_message(request=request, level=messages.SUCCESS, message="Clave y(o)Clave incorrecta")
        return redirect('inicio')

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


def mostar(request):
    pro = Produto.objects.all()
    contexto ={"plato": pro}
    return render(request,'comilon/grid-listing-masonry.html',contexto)


def reg_produc(request):
    nomb = request.POST['nombre']
    prec = request.POST['precio']
    descrip = request.POST['desc']
    empresa = request.POST['emp']
    fotoPla = request.FILES['foto1']

    Produto.objects.create(nombProduc=nomb, precio=prec, descripcion=descrip, Empresa=empresa, 
    imgProd=fotoPla)

    return render(request,'comilon/add-listing-with-menu-list.html')

=======
from django.shortcuts import render, redirect
from .models import Usuario, Rol, Cliente
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.




def index6(request):
    return render(request,'comilon/index-6.html')

def inicio(request):
    return render(request,'comilon/login.html')

def registro(request):
    return render(request,'comilon/register.html')

def user(request):
    return render(request,'comilon/indexUser.html')

def admin(request):
    return render(request,'comilon/index.html')

def menu(request):
    return render(request,'comilon/grid-listing-masonry.html')

def plato (request):
    return render(request,'comilon/detail-restaurant.html')


def inicio_sesion(request):
    cor = request.POST['email']
    cont = request.POST['password']


    try:
        x = Usuario.objects.get(correo = cor, clave = cont)
        rol2 = Rol.objects.get(nombre = "Cliente")

        if x.rol == rol2:
            cli= Cliente.objects.get(rut = x.rut)
            contexto ={"Cliente": x, "datos": cli}

            return render(request,'comilon/indexUser.html',contexto)

        else:
            contexto ={"Administrador": x}
            return render(request,'comilon/index.html',contexto)
    except Usuario.DoesNotExist:
        messages.add_message(request=request, level=messages.SUCCESS, message="Clave y(o)Clave incorrecta")
        return redirect('inicio')

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


def mostar(request):
    pro = Produto.objects.all()
    contexto ={"plato": pro}
    return render(request,'comilon/grid-listing-masonry.html',contexto)


def reg_produc(request):
    nomb = request.POST['nombre']
    prec = request.POST['precio']
    descrip = request.POST['desc']
    empresa = request.POST['emp']
    fotoPla = request.FILES['foto1']

    Produto.objects.create(nombProduc=nomb, precio=prec, descripcion=descrip, Empresa=empresa, 
    imgProd=fotoPla)

    return render(request,'comilon/add-listing-with-menu-list.html')

>>>>>>> Stashed changes
