from django.shortcuts import render, redirect
from .models import habitacion
from .forms import ReservaForm
# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def habitaciones(request):
    habitaciones = habitacion.objects.all()
    data = { 'habitaciones' : habitaciones}
    return render(request, 'app/habitaciones.html', data)

def reserva(request):
    data = { 'form': ReservaForm()}
    return render(request, 'app/reserva.html', data)