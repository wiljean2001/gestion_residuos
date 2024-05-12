# aplicaciones/personal/serializers.py
from rest_framework import serializers
from .models import Vehiculos, Modelos, Marcas


class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = "__all__"


class ModelosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelos
        fields = "__all__"


class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = "__all__"
