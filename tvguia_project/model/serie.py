#-*- coding: utf-8 -*-

from django.db import models

from Programa import Programa

class Serie(Programa):
    class Meta:
        pass

    titulo = None
    descripcion = None
    fecha = None
    edad = None
    puntuacion = None
    imagen = None


