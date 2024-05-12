from rest_framework import viewsets, filters
from .models import Ubicaciones, Categorias
from .serializers import UbicacionesSerializer, CategoriasSerializer


class UbicacionesViewSet(viewsets.ModelViewSet):
    queryset = Ubicaciones.objects.all()
    serializer_class = UbicacionesSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ["nombre", "ciudad", "provincia", "categoría"]
    ordering_fields = ["nombre", "ciudad"]


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ["nombre", "ciudad", "provincia", "categoría"]
    ordering_fields = ["nombre", "ciudad"]
