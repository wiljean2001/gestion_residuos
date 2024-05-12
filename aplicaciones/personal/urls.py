# aplicaciones/personal/urls.py
from rest_framework.routers import DefaultRouter
from .views import EmpleadosViewSet, RolesViewSet

router = DefaultRouter()
router.register(r"empleados", EmpleadosViewSet)
router.register(r"roles", RolesViewSet)

urlpatterns = router.urls
