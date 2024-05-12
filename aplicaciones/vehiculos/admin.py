# aplicaciones/vehiculos/admin.py
from django.contrib import admin
from .models import Vehiculos, Modelos, Marcas

admin.site.register(Marcas)
admin.site.register(Modelos)
admin.site.register(Vehiculos)
