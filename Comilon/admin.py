from django.contrib import admin
from .models import Producto, Rol, Usuario, Cliente

# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Producto)
