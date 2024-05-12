# aplicaciones/personal/views.py
from rest_framework import viewsets
from .models import Vehiculos, Modelos, Marcas
from .serializers import VehiculosSerializer, ModelosSerializer, MarcasSerializer


class VehiculosViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculosSerializer


class ModelosViewSet(viewsets.ModelViewSet):
    queryset = Modelos.objects.all()
    serializer_class = ModelosSerializer


class MarcasViewSet(viewsets.ModelViewSet):
    queryset = Marcas.objects.all()
    serializer_class = MarcasSerializer
