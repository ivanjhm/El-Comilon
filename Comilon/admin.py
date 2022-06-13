from django.contrib import admin
from .models import Cliente, Rol, Usuario

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Rol)
admin.site.register(Usuario)