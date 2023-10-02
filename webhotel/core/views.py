from django.shortcuts import render, redirect
from .models import habitacion
from .forms import ClienteForm
# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def habitaciones(request):
    habitaciones = habitacion.objects.all()
    data = { 'habitaciones' : habitaciones}
    return render(request, 'app/habitaciones.html', data)


def reserva(request):
    data = { 'form': ClienteForm()}
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Solicitud de reserva enviada."
        else:
            data['form'] = formulario
    return render(request, 'app/reserva.html', data)


def contacto(request):
    return render(request, 'app/contacto.html')


def habitacionDisponible(request):
    habitaciones = habitacion.objects.all()
    data = { 'habitaciones' : habitaciones}
    return render(request, 'app/habitacionDisponible.html', data)