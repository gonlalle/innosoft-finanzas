import json

from django.http import HttpResponse
from django.shortcuts import render

from necesidades.models import Necesidad, Comite
from inventario.models import Producto

def formNecesidad(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = request.POST

        if Comite.objects.filter(comite=form['comite']).exists():
            comite = Comite.objects.get(comite=form['comite'])
            #producto = Producto.objects.get(producto=form['producto'])
            necesidad = Necesidad(nombre=form["nombre"].strip(), comite=comite, cantidadNecesitada=form["cantidadNecesitada"], descripcion=form["descripcion"])
            necesidad.save()

        return listNecesidad(request)
    else:
        form = Necesidad() # Unbound form

        return render(request, 'necesidades/nuevaNecesidad.html', {'form': form,"comites": Comite.objects.all})

def formComite(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = request.POST

        comite = Comite(comite=form['comite'])

        comite.save()

        return listNecesidad(request)
    else:
        form = Comite() # Unbound form

        return render(request, 'necesidades/nuevaNecesidad.html', {'form': form})

def listNecesidad(request):
    context = {"necesidades": Necesidad.objects.all,"comites": Comite.objects.all}
    return render(request, "necesidades/listadoNecesidades.html", context)

