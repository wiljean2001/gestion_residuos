# aplicaciones/residuos/urls.py

from rest_framework.routers import DefaultRouter
from .views import ResiduosViewSet, TipoResiduosViewSet  # , PrecioResiduosViewSet

router = DefaultRouter()
router.register(r"residuos", ResiduosViewSet)
router.register(r"tipos-residuos", TipoResiduosViewSet)
# router.register(r"precios-residuos", PrecioResiduosViewSet)

urlpatterns = router.urls
