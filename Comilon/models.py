from django.db import models

# Create your models here.
class Resgistro(models.Model):
    rut = models.CharField(max_length=10,primary_key=True, verbose_name='Rut')
    nombres = models.CharField(max_length=50, verbose_name='Nombre')
    apellidos = models.CharField(max_length=50, verbose_name='Apellido')
    correo = models.CharField(max_length=100, verbose_name='correo electrónico')
    clave = models.CharField(max_length=16, verbose_name='Clave')
    
    def __str__(self):
        return self.nombre