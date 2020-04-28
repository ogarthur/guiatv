# -*- coding: utf-8 -*-

from django.db import models

from .programa import Programa


class Documental(models.Model):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=1000, null=True)
    edad = models.IntegerField(default=0)
    puntuacion = models.IntegerField(null=True)
    duracion = models.IntegerField(null=True)
    imagen = models.CharField(max_length=500, null=True)

    programa_emision = models.ForeignKey(Programa, related_name='programa_documental', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
