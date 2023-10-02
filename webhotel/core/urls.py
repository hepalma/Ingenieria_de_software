from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habitaciones', views.habitaciones, name='habitaciones'),
    path('reserva', views.reserva, name='reserva' ),
    path('contacto', views.contacto, name='contacto' ),
    path('habitacionDisponible', views.habitacionDisponible, name='habitacionDisponible'),
]