from django.db import models

# Create your models here.


class Vehiculo(models.Model):
    placa = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    año = models.IntegerField()
    capacidad = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.placa} - {self.modelo}"
