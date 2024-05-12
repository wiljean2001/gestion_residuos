from django.contrib import admin
from .models import (
    Recolecciones,
    # EstadoRecoleccion,
    ResiduoRecolecciones,
) 


admin.site.register(Recolecciones)
# admin.site.register(EstadoRecoleccion)
admin.site.register(ResiduoRecolecciones)
