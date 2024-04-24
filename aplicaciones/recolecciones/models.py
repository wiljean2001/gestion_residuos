from django.db import models

from aplicaciones.personal.models import PersonalRecojo
from aplicaciones.ubicaciones.models import Ubicacion
from aplicaciones.residuos.models import Residuo
from aplicaciones.vehiculos.models import Vehiculo
# Create your models here.


class EquipoRecojo(models.Model):
    recoleccion = models.ForeignKey('Recoleccion', on_delete=models.CASCADE)
    personal = models.ForeignKey(PersonalRecojo, on_delete=models.CASCADE)
    rol_en_recoleccion = models.CharField(
        max_length=8, choices=PersonalRecojo.CHOICES_ROL)

    def __str__(self):
        return f"{self.personal.nombre} como {self.rol_en_recoleccion} en recolección {self.recoleccion.id}"


class Recoleccion(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    residuo = models.ForeignKey(Residuo, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    guia_numero = models.CharField(max_length=255)
    fecha = models.DateField()
    hora_recoleccion = models.TimeField()
    peso_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fecha} - {self.ubicacion.nombre}"
