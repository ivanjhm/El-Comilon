from django.db import models
from django.contrib.auth.models import User

class Rol (models.Model):
    id_Rol = models.AutoField(primary_key=True, verbose_name='Id del Rol')
    nombre = models.CharField(max_length=15, verbose_name='Nombre del Rol')

    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    id_Usuario = models.AutoField(primary_key=True, verbose_name='Id del Ususario')
    correo = models.CharField(max_length=50, verbose_name='Correo del Usuario')
    clave = models.CharField(max_length=16, verbose_name='Clave del Usuario')
    rut = models.CharField(max_length=11, verbose_name='Rut del usuario')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.correo

class Cliente(models.Model):
    rut = models.CharField(max_length=10,primary_key=True, verbose_name='Rut')
    nombres = models.CharField(max_length=50, verbose_name='Nombre')
    apellidos = models.CharField(max_length=50, verbose_name='Apellido')
    correo = models.CharField(max_length=100, verbose_name='correo electrónico')
    
    def _str_(self):
        return self.nombres

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name='Id del produto')
    nombProduc = models.CharField(max_length=50, verbose_name='Nombre del Producto')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion del Producto')
    imgProd = models.ImageField(upload_to="Producto", null=True, blank=True, verbose_name='Imagen del Producto')
    precio = models.IntegerField(verbose_name='Precio del Producto')
    Empresa = models.CharField(verbose_name='Quien preparó el Producto', max_length=100)

    def __str__(self):
        return self.nombProduc

class Order(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.producto.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.producto.price * self.quantity
		return total

class ShippingAddress(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


