from django.urls import path
from .views import index6, mostar, order, reg_produc, inicio, admin, inicio_sesion, register, registrando,menu, plato

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
    path('mostar/',mostar, name="mostar"),
    path('order/',order, name="order"),
]