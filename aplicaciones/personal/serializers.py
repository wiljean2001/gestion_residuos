# aplicaciones/personal/serializers.py
from rest_framework import serializers
from .models import Empleados, Roles


class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = "__all__"


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"
