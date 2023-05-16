from django.urls import path
from . import views

#estas dos lineas son para configurar y poder mostrar las imgs
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
   #ruta de la vista que muesta la pagina html ejemplo.html
    path("", views.pagInicio, name="pagInicio"),
    #la primer parte "inventario" es el nombre que se debe colocar en la url, views.inventario, en este caso "inventario" debe tener el mismo nombre que la funcion que se encuentra en el archivo views.py, y la ultima parte "name" es el nombre que usamos para colocarlo en las etiquetas html "a" en el atributo "href"
    path("inventario", views.inventario, name="pagInventario"),
    path("crear", views.crear, name="pagCrear"),
    path("editar/<int:placa>", views.editar, name="pagEditar"),
    path("eliminar/<int:placa>", views.eliminar, name="pagEliminar"),
    path('buscar/', views.buscarEquipo, name='buscar'),
    

#esta linea nos permite mostrar las imagenes
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
