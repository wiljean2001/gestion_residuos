# aplicaciones/personal/models.py
from django.db import models


class Roles(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personal-roles"  # Especificar el nombre de la tabla en plural

    def __str__(self):
        return self.nombre


class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    rol = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    licencia = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    # direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
    calle = models.CharField(max_length=255, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    provincia = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "personal-empleados"  # Especificar el nombre de la tabla en plural

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rol}"
