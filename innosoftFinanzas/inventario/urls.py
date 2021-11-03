from django.urls import path

from inventario import views

urlpatterns = [
    path("inventario/busqueda_productos/", views.busqueda_productos),
    path("inventario/buscar/", views.buscar),
    path("inventario/necesidad/", views.necesidad),
]