# aplicaciones/ubicaciones/serializers.py

from rest_framework import serializers
from .models import Ubicaciones, Categorias


class UbicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicaciones
        fields = "__all__"


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"
