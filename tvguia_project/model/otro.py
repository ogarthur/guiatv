#-*- coding: utf-8 -*-

from django.db import models

from Programa import Programa

class Otro(Programa):
    class Meta:
        pass

    Titulo = None
    duracion = None
    imagen = None


