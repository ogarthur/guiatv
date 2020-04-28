from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone

from datetime import datetime, timedelta
from tvguia_app.model.programa import Programa
from tvguia_app.model.canal import Canal
import json

def getDuracion(hora_fin , hora_inicio):
    # inicio = datetime.strptime((self.hora_inicio,"%H:i"))
    # fin =  datetime.strptime((self.hora_fin,"%H:i"))
    duracion = hora_fin - hora_inicio

    minutes = divmod(duracion.seconds, 60)
    print('Difference in minutes: ', minutes[0], 'minutes',
          minutes[1], 'seconds')
    return int(minutes[0])



def fill(request):
    now = datetime.now()
    # {'nombre': , 'icono': , 'posicion': }
    canales = [{'nombre': "tve1", 'icono': 'tve1.webp', 'posicion': "1"},
               {'nombre': "tve2", 'icono': 'tve2.webp', 'posicion': "2"},

               ]
    programas = [
        {
        'hora_inicio': now,
        'hora_fin': now + timedelta(hours=2),
        'titulo':"Pear Harbor",
        'descripcion':"pelicula belica sobre el ataque sorpresa de pear harbor",
        'imagen':"poster1.jpg",
        'tipo':"pelicula",
        'canal_emision': "tve1",
        'duracion_total': getDuracion((now + timedelta(hours=2)), now)
        },
        {
            'hora_inicio': now+ timedelta(hours=2),
            'hora_fin': now + timedelta(hours=4),
            'titulo': "Pear Harbor",
            'descripcion': "pelicula belica sobre el ataque sorpresa de pear harbor",
            'imagen': "poster1.jpg",
            'tipo': "pelicula",
            'canal_emision': "tve1",
            'duracion_total': getDuracion((now + timedelta(hours=4)),  now+ timedelta(hours=2))
        },
        {
            'hora_inicio': now + timedelta(hours=4),
            'hora_fin': now + timedelta(hours=6),
            'titulo': "Pear Harbor",
            'descripcion': "pelicula belica sobre el ataque sorpresa de pear harbor",
            'imagen': "poster1.jpg",
            'tipo': "pelicula",
            'canal_emision': "tve1",
            'duracion_total': getDuracion((now + timedelta(hours=6)), now + timedelta(hours=4))
        },
        {
            'hora_inicio': now + timedelta(hours=8),
            'hora_fin': now + timedelta(hours=10),
            'titulo': "Pear Harbor",
            'descripcion': "pelicula belica sobre el ataque sorpresa de pear harbor",
            'imagen': "poster1.jpg",
            'tipo': "pelicula",
            'canal_emision': "tve1",
            'duracion_total': getDuracion((now + timedelta(hours=10)), now + timedelta(hours=8))
        },


    {
        'hora_inicio': now - timedelta(hours=2),
        'hora_fin': now,
        'titulo':"starshiptroopers",
        'descripcion':"guerra de arañas",
        'imagen':"poster2.jpg",
        'tipo':"pelicula",
        'canal_emision':"tve1",
         'duracion_total': getDuracion(now,( now - timedelta(hours=2)))
    },
    {
        'hora_inicio': now+ timedelta(hours=2),
        'hora_fin': now + timedelta(hours=3),
        'titulo':"seriesinimage",
        'descripcion': "prueba",
        'imagen': "poster1.jpg",
        'tipo':"serie",
        'canal_emision':"tve2",
        'duracion_total': getDuracion((now + timedelta(hours=3)), (now + timedelta(hours=2)))
    }
    ]




    # INSERTAR CANALES
    canal_bulk = []
    for canal in canales:
        if not Canal.objects.filter(nombre=canal['nombre']).exists():
            new_canal = Canal()
            new_canal.nombre = canal['nombre']
            new_canal.icono = canal['icono']
            new_canal.posicion = canal['posicion']
            canal_bulk.append(new_canal)
    Canal.objects.bulk_create(canal_bulk)

    # INSERTAR PROGRAMAS
    programa_bulk = []
    for programa in programas:
        print(programa['hora_inicio'])
        if not Programa.objects.filter(hora_inicio=programa['hora_inicio']).exists():
            print("no existe programa en esa hora")
            new_programa = Programa()
            new_programa.hora_inicio = programa['hora_inicio']
            new_programa.hora_fin = programa['hora_fin']
            new_programa.titulo = programa['titulo']
            new_programa.descripcion = programa['descripcion']
            new_programa.imagen = programa['imagen']
            new_programa.tipo = programa['tipo']
            new_programa.duracion_total = programa['duracion_total']
            new_programa.canal_emision = Canal.objects.get(nombre=programa['canal_emision'])
            programa_bulk.append(new_programa)
    Programa.objects.bulk_create(programa_bulk)
    return render(request, 'tvguia_app/home.html')


if __name__== "__main__":
    fill()
