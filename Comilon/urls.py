from django.urls import path
from .views import cart, updateItem, processOrder, checkout,index6, reg_produc, inicio, admin, inicio_sesion, register, registrando,menu, store

urlpatterns = [

    path('',index6, name="index-6"),
    path('inicio/',inicio, name="inicio"),
    path('user/',inicio_sesion, name="user"),
    path('admin/',admin, name="admin"),
    path('register/',register, name="register"),
    path('reg/',registrando, name="reg"),
    path('menu/',menu, name="menu"),
    path('reg_produc/',reg_produc, name="reg_produc"),
    path('store/', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('update_item/', updateItem, name="update_item"),
	path('process_order/', processOrder, name="process_order"),
]