from django.contrib import admin
from django.urls import path, include
from aplicaciones.core.views import CustomTokenObtainPairView

admin.site.site_header = "Tutorial Admin"
admin.site.index_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('activate/', include('aplicaciones.core.urls')),
    path('auth/jwt/create/', CustomTokenObtainPairView.as_view(),
         name='custom_jwt_create'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]