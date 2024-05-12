# aplicaciones/personal/urls.py
from rest_framework.routers import DefaultRouter
from .views import VehiculosViewSet, ModelosViewSet, MarcasViewSet

router = DefaultRouter()
router.register(r"vehiculos", VehiculosViewSet)
router.register(r"modelos", ModelosViewSet)
router.register(r"marcas", MarcasViewSet)

urlpatterns = router.urls
