# aplicaciones/recolecciones/urls.py
from rest_framework.routers import DefaultRouter
from .views import RecoleccionesViewSet, ResiduoRecoleccionesViewSet

router = DefaultRouter()
router.register(r"recolecciones", RecoleccionesViewSet)
router.register(r"residuo-recolecciones", ResiduoRecoleccionesViewSet)

urlpatterns = router.urls
