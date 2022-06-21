import json
from .models import *

def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in cart:
		try:	
			if(cart[i]['quantity']>0): #items with negative quantity = lot of freebies  
				cartItems += cart[i]['quantity']
				producto = Producto.objects.get(id=i)
				total = (producto.price * cart[i]['quantity'])
				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]['quantity']
				item = {
				'id':producto.id,
				'product':{'id':producto.id,'name':producto.nombProduc, 'price':producto.precio, 
				'imageURL':producto.imgProd}, 'quantity':cart[i]['quantity'],'get_total':total,
				}
				items.append(item)
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	
	order, created = Order.objects.get_or_create( complete=False)
	items = order.orderitem_set.all()
	cartItems = order.get_cart_items

	return {'cartItems':cartItems ,'order':order, 'items':items}

	
def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Producto.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
		)
	return customer, order
