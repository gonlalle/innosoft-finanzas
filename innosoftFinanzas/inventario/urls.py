from django.urls import path

from . import views

#We should normalize and add all urls to the main app "innosoftFinanzas"

urlpatterns = [
    path('', views.index,name="inventario"),
    path('<int:num>', views.index,name="inventario"),
]