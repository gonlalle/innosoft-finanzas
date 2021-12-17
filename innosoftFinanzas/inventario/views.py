from django.shortcuts import render
from usuarios.models import Usuario
# Create your views here.
def formProducto(request):
    context = {}

    return render(request,"inventario/formulario.html",context)