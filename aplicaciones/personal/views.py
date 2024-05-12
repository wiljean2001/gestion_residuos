# aplicaciones/personal/views.py
from rest_framework import viewsets
from .models import Empleados, Roles
from .serializers import EmpleadosSerializer, RolesSerializer


class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
