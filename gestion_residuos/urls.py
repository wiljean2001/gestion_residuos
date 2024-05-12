from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
from django.views.generic import TemplateView

# from aplicaciones.core.views import CustomTokenObtainPairView

admin.site.site_header = "Tutorial Admin"
admin.site.index_title = "Admin"


# def index_view(request):
#     return render(request, "dist/index.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", index_view, name="index"),
    path(
        "api/",
        include(
            [
                path("activate/", include("aplicaciones.core.urls")),
                # path(
                #     "auth/jwt/create/",
                #     CustomTokenObtainPairView.as_view(),
                #     name="custom_jwt_create",
                # ),
                path("auth/", include("djoser.urls")),
                path("auth/", include("djoser.urls.jwt")),
                # Añadir rutas para otras aplicaciones de la API
                path("empleados/", include("aplicaciones.personal.urls")),
                path("vehiculos/", include("aplicaciones.vehiculos.urls")),
                path("ubicaciones/", include("aplicaciones.ubicaciones.urls")),
                path("recolecciones/", include("aplicaciones.recolecciones.urls")),
                path("residuos/", include("aplicaciones.residuos.urls")),
                path("personal/", include("aplicaciones.personal.urls")),
                # Continuar con otras aplicaciones necesarias
            ]
        ),
    ),
    # path(
    #     "", TemplateView.as_view(template_name="dist/index.html"), name="index"
    # ),  # Ruta inicial
    # re_path(
    #     r"^(?:.*)/?$", TemplateView.as_view(template_name="dist/index.html")
    # ),  # Captura todas las otras rutas
]


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("activate/", include("aplicaciones.core.urls")),
#     path(
#         "auth/jwt/create/",
#         CustomTokenObtainPairView.as_view(),
#         name="custom_jwt_create",
#     ),
#     path("auth/", include("djoser.urls")),
#     path("auth/", include("djoser.urls.jwt")),
#     path("", index_view, name="index"),
# ]
