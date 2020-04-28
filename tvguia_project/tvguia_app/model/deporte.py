# -*- coding: utf-8 -*-

from django.db import models

from .programa import Programa


class Deporte(models.Model):
    class Meta:
        pass

    titulo = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=1000, null=True)
    imagen = models.CharField(max_length=500, null=True)

    programa_emision = models.ForeignKey(Programa, related_name='programa_deporte', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo;
