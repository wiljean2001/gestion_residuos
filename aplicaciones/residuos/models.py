from django.db import models


class TipoResiduos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "residuos-tiporesiduos"  # Ajustando el nombre en el admin a plural


""" Solo si los precios de los reciduos deben trabajarse por grupos o de forma individual """
# class PrecioResiduos(models.Model):
#     tipo_residuo = models.ForeignKey(
#         TipoResiduos, on_delete=models.CASCADE, related_name="precios"
#     )
#     precio_por_kg = models.DecimalField(max_digits=6, decimal_places=2)
#     fecha_inicio_vigencia = models.DateField()
#     fecha_fin_vigencia = models.DateField(null=True, blank=True)
#     creado_en = models.DateTimeField(auto_now_add=True)
#     actualizado_en = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.tipo_residuo.nombre} - {self.precio_por_kg} por kg"

# class Meta:
#     verbose_name_plural = "precio"  # Ajustando el nombre en el admin a plural


class Residuos(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(
        TipoResiduos, on_delete=models.CASCADE, related_name="residuos"
    )
    descripcion = models.TextField(blank=True, null=True)
    fecha_recoleccion = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo.nombre})"

    class Meta:
        verbose_name_plural = (
            "residuos-residuos"  # Ajustando el nombre en el admin a plural
        )
