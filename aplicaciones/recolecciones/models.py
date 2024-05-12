from django.db import models
from aplicaciones.personal.models import Empleados
from aplicaciones.ubicaciones.models import Ubicaciones
from aplicaciones.residuos.models import Residuos
from aplicaciones.vehiculos.models import Vehiculos


class EstadoRecoleccion(models.TextChoices):
    PENDIENTE = "Pendiente", "Pendiente"
    EN_PROGRESO = "En Progreso", "En Progreso"
    COMPLETADA = "Completada", "Completada"
    CANCELADA = "Cancelada", "Cancelada"


class Recolecciones(models.Model):
    fecha_programada = models.DateField()
    fecha_realizada = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=EstadoRecoleccion.choices,
        default=EstadoRecoleccion.PENDIENTE,
    )
    vehiculo = models.ForeignKey(
        Vehiculos, on_delete=models.SET_NULL, null=True, related_name="recolecciones"
    )
    conductor = models.ForeignKey(
        Empleados,
        on_delete=models.SET_NULL,
        null=True,
        related_name="recolecciones_como_conductor",
    )
    ayudantes = models.ManyToManyField(
        Empleados, related_name="recolecciones_como_ayudante", blank=True
    )
    ubicacion = models.ForeignKey(
        Ubicaciones, on_delete=models.SET_NULL, null=True, related_name="recolecciones"
    )

    def __str__(self):
        return f"Recolección {self.id} - {self.fecha_programada} ({self.estado})"

    class Meta:
        verbose_name_plural = (
            "recolecciones-recolecciones"  # Ajustando el nombre en el admin a plural
        )


class ResiduoRecolecciones(models.Model):
    recoleccion = models.ForeignKey(
        Recolecciones, on_delete=models.CASCADE, related_name="residuos"
    )
    residuo = models.ForeignKey(
        Residuos, on_delete=models.CASCADE, related_name="recolecciones"
    )
    peso = models.FloatField(help_text="Peso en kilogramos")

    def __str__(self):
        return f"{self.residuo} ({self.peso} kg) en {self.recoleccion}"

    class Meta:
        verbose_name_plural = "recolecciones-residuorecolecciones"  # Ajustando el nombre en el admin a plural
