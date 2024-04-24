from django.db import models

# Create your models here.


class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    zona = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
