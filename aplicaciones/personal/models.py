from django.db import models


class PersonalRecojo(models.Model):
    CHOICES_ROL = (
        ('chofer', 'Chofer'),
        ('ayudante', 'Ayudante'),
    )

    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=8, choices=CHOICES_ROL)
    # Nullable para ayudantes
    licencia = models.CharField(max_length=255, null=True, blank=True)
    fecha_nacimiento = models.DateField()
    contacto = models.CharField(max_length=255)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} ({self.rol})"
