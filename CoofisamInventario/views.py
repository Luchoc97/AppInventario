from django.shortcuts import render, redirect
from django.http import HttpResponse
#importamos el modelo "Equipos" para traer la informacion que tiene dicho modelo
from .models import Equipos
from .forms import EquipoForm
# Create your views here.

#esta funcion recibe una peticion(request) e imprime o retorna una pagina html, se debe especificar la ruta donde se encuentra dicha pagina, la ruta es "templates/paginas/index.html", "templates" no es necesario colocarlo ya que django lo toma automaticamente
def pagInicio(request):
    return render(request, "paginas/index.html")

def inventario(request):
    #variable que guarda la consulta de todos los registros que hay en el modelo "Equipos"
    invEquipos = Equipos.objects.all()
    #con "invEquipos": invEquipos, cabe aclara que deben tener el mismo nombre '"invEquipos": invEquipos', ya podremos mostrar los datos que hay en esa consulta en el "inventario/index.html"
    return render(request, "inventario/index.html", {"invEquipos": invEquipos})

def crear(request):
    #solicita la informacion y archivos
    formulario = EquipoForm(request.POST or None, request.FILES or None)
    #si el formulario es valido, es decir los campos se ha digitado informacion, se guardaran los datos y lo redirige a la vista del inventario
    if formulario.is_valid():
        formulario.save()
        return redirect("pagInventario")
    return render(request, "inventario/crear.html", {"formulario": formulario})

#actualiza el registro por id
def editar(request, placa):
    equipo = Equipos.objects.get(placa=placa)
    formulario = EquipoForm(request.POST or None, request.FILES or None, instance=equipo)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("pagInventario")
    return render(request, "inventario/editar.html", {"formulario": formulario})

#elimina registro por id y redirige a la pagina del inventario
def eliminar(request, placa):
    equipo = Equipos.objects.get(placa=placa)
    equipo.delete()
    return redirect("pagInventario")

#consulta por placa, se filtran los registros por placa, si la consulta es valida muestra el registro que coincide. Renderiza el resultado en la pagina index de inventario
def buscarEquipo(request):
    query = request.GET.get('consulta', '')  # Obtiene el parámetro 'consulta' de la URL
    resultados = Equipos.objects.filter(placa__icontains=query) if query else Equipos.objects.all()
    return render(request, 'inventario/index.html', {'resultados': resultados, 'query': query})