<<<<<<< Updated upstream
from django.urls import path
from .views import index6, reg_produc, inicio, registro, user, admin, inicio_sesion, register, registrando,menu, plato

urlpatterns = [

    path('',index6, name="index-6"),
    path('inicio/',inicio, name="inicio"),
    path('user/',inicio_sesion, name="user"),
    path('admin/',admin, name="admin"),
    path('register/',register, name="register"),
    path('reg/',registrando, name="reg"),
    path('menu/',menu, name="menu"),
    path('plato/',plato, name="plato"),
    path('reg_produc/',reg_produc, name="reg_produc"),
=======
from django.urls import path
from .views import index6, reg_produc, inicio, registro, user, admin, inicio_sesion, register, registrando,menu, plato

urlpatterns = [

    path('',index6, name="index-6"),
    path('inicio/',inicio, name="inicio"),
    path('user/',inicio_sesion, name="user"),
    path('admin/',admin, name="admin"),
    path('register/',register, name="register"),
    path('reg/',registrando, name="reg"),
    path('menu/',menu, name="menu"),
    path('plato/',plato, name="plato"),
    path('reg_produc/',reg_produc, name="reg_produc"),
>>>>>>> Stashed changes
]