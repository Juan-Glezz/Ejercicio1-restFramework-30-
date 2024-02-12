from django.db import models


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Marcas"


class Vehiculo(models.Model):
    tipo_vehiculo = (
        ('Coche', 'Coche'),
        ('Ciclomotor', 'ciclomotor'),
        ('Motocicleta', 'Motocicleta'),
    )
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    tipoVehiculo = models.CharField(max_length=100, choices=tipo_vehiculo)
    matricula = models.CharField(max_length=100, unique=True)
    suspendido = models.BooleanField(default=False)
    fecha_fabricacion = models.DateField()
    fecha_baja = models.DateField()
    fecha_matricula = models.DateField()
    chasis = models.IntegerField()
