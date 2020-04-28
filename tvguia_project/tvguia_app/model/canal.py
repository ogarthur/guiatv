#-*- coding: utf-8 -*-

from django.db import models


class Canal(models.Model):
    class Meta:
        pass

    nombre = models.CharField(max_length=100, unique=True)
    icono = models.CharField(max_length=500, null=True)
    posicion = models.IntegerField(unique=True)

    def __str__(self):
        return self.nombre;

