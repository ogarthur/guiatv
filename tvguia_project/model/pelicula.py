#-*- coding: utf-8 -*-

from django.db import models

from Programa import Programa

class Pelicula(Programa):
    class Meta:
        pass

    titulo = None
    fecha = None
    descripcion = None
    edad = None
    puntuacion = None
    duracion = None
    imagen = None

     = models.OneToOneField('Programa')

