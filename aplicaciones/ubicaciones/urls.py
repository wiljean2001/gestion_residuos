# aplicaciones/ubicaciones/urls.py

from rest_framework.routers import DefaultRouter
from .views import UbicacionesViewSet, CategoriasViewSet

router = DefaultRouter()
router.register(r"ubicaciones", UbicacionesViewSet)
router.register(r"categorias", CategoriasViewSet)

urlpatterns = router.urls
