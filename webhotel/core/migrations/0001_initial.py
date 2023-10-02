# Generated by Django 4.2.5 on 2023-10-02 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False, verbose_name='Id cliente')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre cliente')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido cliente')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo cliente')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono cliente')),
            ],
        ),
        migrations.CreateModel(
            name='estado',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False, verbose_name='Id estado')),
                ('nombreEstado', models.CharField(max_length=20, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='habitacion',
            fields=[
                ('idHabitacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id habitacion')),
                ('tipoHabitacion', models.CharField(max_length=50, verbose_name='tipo habitacion')),
                ('capacidadHabitacion', models.CharField(max_length=50, verbose_name='Capacidad habitacion')),
                ('precioHabitacion', models.CharField(max_length=50, verbose_name='precio habitacion')),
                ('descripcionHabitacion', models.TextField(max_length=2000, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('idHotel', models.AutoField(primary_key=True, serialize=False, verbose_name='Id hotel')),
                ('nombreHotel', models.CharField(max_length=50, verbose_name='Nombre hotel')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion hotel')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('idReserva', models.AutoField(primary_key=True, serialize=False, verbose_name='Id reserva')),
                ('fechaArribo', models.DateField(verbose_name='Fecha arribo')),
                ('fechaPartida', models.DateField(verbose_name='Fecha salida')),
                ('cantidadPersonas', models.CharField(max_length=50, verbose_name='Cantidad personas')),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('idHabitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.habitacion')),
            ],
        ),
        migrations.AddField(
            model_name='habitacion',
            name='idHotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hotel'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='nombreEstado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estado'),
        ),
    ]
