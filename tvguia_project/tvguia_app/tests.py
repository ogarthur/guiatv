from django.test import TestCase

from tvguia_app.model.canal import Canal
from .model.programa import Programa
# Create your tests here.


Canal.objects.create(nombre="tve1",icono="../static/images/iconos/tve1.webp",posicion="1")