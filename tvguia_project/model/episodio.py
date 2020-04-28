#-*- coding: utf-8 -*-

from django.db import models

class Episodio(models.Model):
    class Meta:
        pass

    titulo = None
    descripcion = None
    duracion = None
    numero = None
    temporada = None


