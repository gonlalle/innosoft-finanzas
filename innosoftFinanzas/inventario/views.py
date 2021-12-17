from django.shortcuts import render

from inventario.models import Producto,Categoria
# Create your views here.
def formProducto1(request):
    context = {}

    return render(request, "inventario/nuevoProducto.html", context)

def formProducto(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = request.POST

        if Categoria.objects.filter(categoria=form['categoria']).exists():
            categoria = Categoria.objects.get(categoria=form['categoria'])
            producto = Producto(nombre=form["nombre"].strip(), categoria=categoria, unidades=form["unidades"], valorMonetario=form["valorMonetario"], descripcion=form["descripcion"])
            producto.save()

            return listProducto(request)
    else:
        form = Producto() # Unbound form

    return render(request, 'inventario/nuevoProducto.html', {'form': form,"categorias": Categoria.objects.all})

def listProducto(request):
    context = {"productos": Producto.objects.all}
    return render(request, "inventario/listadoProductos.html", context)

def eliminarProducto(request, id):
    context = {}

    if Producto.objects.filter(id=id).exists():
        producto = Producto.objects.get(id=id)
        producto.delete()
        return listProducto(request)
    else:
        return listProducto(request)

def eliminarCategoria(request, id):
    context = {}

    if Producto.objects.filter(id=id).exists():
        producto = Producto.objects.get(id=id)
        producto.delete()
        return listProducto(request)
    else:
        return listProducto(request)
