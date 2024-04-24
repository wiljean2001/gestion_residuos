from django.db import models

# Create your models here.

class Residuo(models.Model):
    tipo = models.CharField(max_length=100)
    fecha_recoleccion = models.DateField()
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_medida = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    peligrosidad = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    moneda = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.cantidad} {self.unidad_medida}"
