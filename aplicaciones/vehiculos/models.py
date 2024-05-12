# aplicaciones/vehiculos/models.py
from django.db import models


class Marcas(models.Model):
    nombre = models.CharField(max_length=50)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehiculos-marcas"  # Especificar el nombre de la tabla en plural

    def __str__(self):
        return self.nombre


class Modelos(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehiculos-modelos"  # Especificar el nombre de la tabla en plural

    def __str__(self):
        return f"{self.marca.nombre} {self.nombre}"


class Vehiculos(models.Model):
    tipo = models.CharField(
        max_length=20,
        choices=[
            ("CAMION", "Camión"),
            ("FURGONETA", "Furgoneta"),
            ("CAMIONETA", "Camioneta"),
            ("REMOLQUE", "Remolque"),
        ],
    )
    modelo = models.ForeignKey(Modelos, on_delete=models.CASCADE)
    placa = models.CharField(max_length=20, unique=True)
    capacidad_carga = models.FloatField(help_text="Capacidad en toneladas")
    fecha_adquisicion = models.DateField()
    en_servicio = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehiculos-vehiculos"  # Especificar el nombre de la tabla en plural

    def __str__(self):
        return f"{self.modelo} - {self.placa}"
