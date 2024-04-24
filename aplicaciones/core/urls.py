from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('exists', views.check_username_exists, name='exists'),
    path('home', views.home, name='home'),
]
