from rest_framework import viewsets, filters
from .models import TipoResiduos, Residuos  # , PrecioResiduos
from .serializers import (
    TipoResiduosSerializer,
    # PrecioResiduosSerializer,
    ResiduosSerializer,
)


class TipoResiduosViewSet(viewsets.ModelViewSet):
    queryset = TipoResiduos.objects.all()
    serializer_class = TipoResiduosSerializer


# class PrecioResiduosViewSet(viewsets.ModelViewSet):
#     queryset = PrecioResiduos.objects.all()
#     serializer_class = PrecioResiduosSerializer


class ResiduosViewSet(viewsets.ModelViewSet):
    queryset = Residuos.objects.all()
    serializer_class = ResiduosSerializer
