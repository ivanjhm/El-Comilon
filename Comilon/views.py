import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Producto, ShippingAddress, Usuario, Rol, Cliente, OrderItem, Order
from django.contrib import messages
from .utils import cookieCart, cartData, guestOrder

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
    return render(request,'comilon/catalogo.html')

def plato (request):
    return render(request,'comilon/detail-restaurant.html')

def order(request):
    return render(request,'comilon/order.html')

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

def reg_produc(request):
    nomb = request.POST['nombre']
    prec = request.POST['precio']
    descrip = request.POST['desc']
    empresa = request.POST['emp']
    fotoPla = request.FILES['foto1']

    Producto.objects.create(nombProduc=nomb, precio=prec, descripcion=descrip, Empresa=empresa, 
    imgProd=fotoPla)

    return render(request,'comilon/add-listing-with-menu-list.html')

def store(request):
	data = cartData(request)
	cartItems = data['cartItems']
	producto = Producto.objects.all()
	context = {'producto':producto, 'cartItems':cartItems}
	return render(request, 'comilon/store.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'comilon/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'comilon/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Producto.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
