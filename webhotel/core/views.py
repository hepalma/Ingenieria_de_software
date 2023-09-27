from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def habitaciones(request):
    return render(request, 'app/habitaciones.html')