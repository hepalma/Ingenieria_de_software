from django.contrib import admin
from .models import cliente, hotel, habitacion, reserva
# Register your models here.

class ClientSetting(admin.ModelAdmin):
    list_display = ["idCliente", "nombre", "apellido", "correo", "telefono"]
    list_editable = ["nombre", "apellido", "correo", "telefono"]
    list_filter = ["idCliente", "nombre"]


class HotelSetting(admin.ModelAdmin):
    list_display = ["idHotel", "nombreHotel", "direccion", "categoria"]
    list_editable = ["nombreHotel", "direccion", "categoria"]


class HabitacionSetting(admin.ModelAdmin):
    list_display = ["idHabitacion", "idHotel", "tipoHabitacion", "capacidadHabitacion", "precioHabitacion", "descripcionHabitacion", "estadoHabitacion"]
    list_editable = ["tipoHabitacion", "capacidadHabitacion", "precioHabitacion", "descripcionHabitacion", "estadoHabitacion"]
    list_filter = ["tipoHabitacion", "capacidadHabitacion", "precioHabitacion", "estadoHabitacion"]



class ReservaSetting(admin.ModelAdmin):
    list_display = ["idReserva", "idHabitacion", "idCliente", "fechaArribo", "fechaPartida", "cantidadPersonas"]
    list_editable = ["fechaArribo", "fechaPartida", "cantidadPersonas"]
    list_filter = ["fechaArribo", "fechaPartida", "cantidadPersonas"]



admin.site.register(reserva, ReservaSetting)
admin.site.register(habitacion, HabitacionSetting)
admin.site.register(hotel, HotelSetting)
admin.site.register(cliente, ClientSetting)