from django.shortcuts import render

# Create your views here.


def index6(request):
    return render(request,'comilon/index-6.html')

def inicio(request):
    return render(request,'comilon/login.html')


def register(request):
    return render(request,'comilon/register.html')