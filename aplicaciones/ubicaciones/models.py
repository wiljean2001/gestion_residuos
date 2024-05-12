# aplicaciones/ubicaciones/models.py
from django.db import models


class Categorias(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ubicaciones-categorias"


class Ubicaciones(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    distrito = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10, blank=True)
    categoria = models.ForeignKey(
        Categorias, on_delete=models.SET_NULL, null=True, blank=True
    )  # Ejemplo: Comercial, Residencial, Industrial

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}, {self.provincia}, {self.distrito}"

    class Meta:
        verbose_name_plural = (
            "ubicaciones-ubicaciones"  # Ajustando el nombre en el admin a plural
        )
