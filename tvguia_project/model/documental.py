#-*- coding: utf-8 -*-

from django.db import models

from Programa import Programa

class Documental(Programa):
    class Meta:
        pass

    titulo = None
    descripcion = None
    fecha = None
    edad = None
    puntuacion = None
    duracion = None
    imagen = None


