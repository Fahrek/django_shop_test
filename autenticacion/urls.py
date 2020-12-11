from django.urls import path
from .views import VistaRegistro, acceder, salir

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/', salir, name="salir"),
]
