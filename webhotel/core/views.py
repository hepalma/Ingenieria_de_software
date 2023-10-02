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
    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data ["mensaje"] = "Solicitud de reserva enviada."
        else:
            data['form'] = formulario
    return render(request, 'app/reserva.html', data)


def contacto(request):
    return render(request, 'app/contacto.html')