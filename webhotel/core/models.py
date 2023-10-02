from django.db import models

# Create your models here.
class cliente(models.Model):
    idCliente= models.AutoField(primary_key=True, verbose_name="Id cliente")
    nombre = models.CharField(max_length=50, verbose_name="Nombre cliente")
    apellido = models.CharField(max_length=50, verbose_name="apellido cliente")
    correo = models.CharField(max_length=50, verbose_name="Correo cliente")
    telefono = models.CharField(max_length=9, verbose_name="Telefono cliente")

    def __str__(self):
        return str(self.idCliente)
    


class hotel(models.Model):
    idHotel= models.AutoField(primary_key=True, verbose_name="Id hotel")
    nombreHotel = models.CharField(max_length=50, verbose_name="Nombre hotel")
    direccion = models.CharField(max_length=50, verbose_name="Direccion hotel")
    categoria = models.CharField(max_length=50, verbose_name="Categoria Hotel")

    def __str__(self):
        return str(self.idHotel)
    

class estado(models.Model):
    idEstado = models.AutoField(primary_key=True, verbose_name="Id estado")
    nombreEstado = models.CharField(max_length=20, verbose_name="Estado")

    def __str__(self):
        return str(self.idEstado)


class habitacion(models.Model):
    idHabitacion= models.AutoField(primary_key=True, verbose_name="Id habitacion")
    idHotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    tipoHabitacion = models.CharField(max_length=50, verbose_name="tipo habitacion")
    capacidadHabitacion = models.CharField(max_length=50, verbose_name="Capacidad habitacion")
    precioHabitacion = models.CharField(max_length=50, verbose_name="precio habitacion")
    descripcionHabitacion = models.TextField(max_length=2000, verbose_name="descripcion")
    nombreEstado = models.ForeignKey(estado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idHabitacion)


class reserva(models.Model):
    idReserva= models.AutoField(primary_key=True, verbose_name="Id reserva")
    idHabitacion = models.ForeignKey(habitacion, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    fechaArribo = models.DateField(verbose_name="Fecha arribo")
    fechaPartida = models.DateField(verbose_name="Fecha salida")
    cantidadPersonas = models.CharField(max_length=50, verbose_name="Cantidad personas")

    def __str__(self):
        return str(self.idHabitacion)