# aplicaciones/residuos/serializers.py

from rest_framework import serializers
from .models import TipoResiduos, Residuos #, PrecioResiduos


class TipoResiduosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoResiduos
        fields = "__all__"


class ResiduosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residuos
        fields = "__all__"


# class PrecioResiduosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrecioResiduos
#         fields = "__all__"
