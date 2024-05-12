# aplicaciones/recolecciones/serializers.py

from rest_framework import serializers
from .models import Recolecciones, ResiduoRecolecciones


class ResiduoRecoleccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResiduoRecolecciones
        fields = ["id", "recoleccion", "residuo", "peso"]


class RecoleccionesSerializer(serializers.ModelSerializer):
    residuos = ResiduoRecoleccionesSerializer(many=True, read_only=True)

    class Meta:
        model = Recolecciones
        fields = [
            "id",
            "fecha_programada",
            "fecha_realizada",
            "estado",
            "vehiculo",
            "conductor",
            "ayudantes",
            "ubicacion",
            "residuos",
        ]
