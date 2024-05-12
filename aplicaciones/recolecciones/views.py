from rest_framework import viewsets
from .models import Recolecciones, ResiduoRecolecciones
from .serializers import RecoleccionesSerializer, ResiduoRecoleccionesSerializer


class RecoleccionesViewSet(viewsets.ModelViewSet):
    queryset = Recolecciones.objects.all()
    serializer_class = RecoleccionesSerializer


class ResiduoRecoleccionesViewSet(viewsets.ModelViewSet):
    queryset = ResiduoRecolecciones.objects.all()
    serializer_class = ResiduoRecoleccionesSerializer
