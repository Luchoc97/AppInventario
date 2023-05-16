from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
#el modelo es la tabla y sus respectivos campos
class Equipos(models.Model):
    #campo identificador llave primaria autoincremental
    #id = models.AutoField(primary_key=True)
    #null=False, blank=False indica que se debe digitar informacion, ademas que este campo es llave primaria por lo cual es obligatorio tambien por esa caracteristica
    placa = models.IntegerField(primary_key=True, verbose_name='Placa', null=False, blank=False)
    #campo de texto con una longitud maxima de 100 caracteres, verbose_name='Marca' nos permite mostrar la informacion que tiene ese campo
    marca = models.CharField(max_length=100, verbose_name='Marca')
    referencia= models.CharField(max_length=100, verbose_name='Referencia')
    especificaciones= models.TextField(max_length=100, verbose_name='Especificaciones', blank=True, null=True, default="")
    persona= models.CharField(max_length=100, verbose_name='Persona', blank=True, null=True, default="")
    observaciones= models.CharField(max_length=200, verbose_name='Observaciones', blank=True, null=True, default="")
    foto = models.ImageField(upload_to='fotos/', verbose_name='Foto', blank=True, null=True, default="")
    
    #mostramos los datos que se han insertado de la siguiente manera
    """def __str__(self):
        datos = "Placa: " + str(self.placa) + "-" + "Marca: " + self.marca + "-" + "Referencia: " + self.referencia + "-" + "Especificaciones: " + self.especificaciones + "-" + "Persona: " + self.persona + "-" + "Observaciones: " + self.observaciones
        return datos"""
    
    def __str__(self):
        datos = "Placa: " + str(self.placa) + "-" + "Marca: " + self.marca + "-" + "Referencia: " + self.referencia + "-" + "Especificaciones: " + self.especificaciones
        #se coloca en condional estos campos ya que cuando no se digita nada toma como valor "None" por lo cual lo hago asi para evitar errores
        if self.persona:
            datos += " - Persona: " + self.persona
        if self.observaciones:
            datos += " - Observaciones: " + self.observaciones
        return datos
    
    #con este bloque indicamos que borraremos la imagen almacenada tomando el nombre de la imagen, ya que si tenemos este bloque de codigo cuando se elimine le registro se borrarán los datos pero la imagen seguira almacenada en el servidor
    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()