from django.http.response import HttpResponse
from django.shortcuts import render
from inventario.models import Producto

# Create your views here.
def busqueda_productos(request):
    return render(request, "formulario.html")

def buscar(request):

    if request.GET["producto"]:

        producto = request.GET["producto"]

        productos = Producto.objects.filter(nombre__icontains=producto)

        return render(request, "resultados_busqueda.html", {"productos": productos, "query": producto})
    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)

def necesidad(request):
    if request.method == "POST":
        return render(request, "done.html")

    return render(request, "formulario_necesidad.html")