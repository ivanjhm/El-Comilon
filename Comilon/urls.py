from django.urls import path
from .views import index6, inicio, registrando, register

urlpatterns = [

    path('',index6, name="index-6"),
    path('inicio/',inicio, name="inicio"),
    path('register/',register, name="register"),
    path('reg/',registrando, name="reg"),
]