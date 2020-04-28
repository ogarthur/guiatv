from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.utils import timezone

from datetime import datetime, timedelta
from ..model.programa import Programa
from ..model.canal import Canal

from django.contrib.auth.decorators import login_required
from ..decorators import superuser_only

import json


def getDuracion(hora_fin , hora_inicio):
    # inicio = datetime.strptime((self.hora_inicio,"%H:i"))
    # fin =  datetime.strptime((self.hora_fin,"%H:i"))
    duracion = hora_fin - hora_inicio

    minutes = divmod(duracion.seconds, 60)
    print('Difference in minutes: ', minutes[0], 'minutes',
          minutes[1], 'seconds')
    return int(minutes[0])


def index(request, dia="hoy"):
    """  MAIN PAGE """
    now = timezone.now()
    hoy = now.strftime("%d")
   # hora_actual = now.strftime("%H:i")
    hora_actual = now
    '''dev comment'''

    hoy = '14'
    if dia == "hoy":
        fecha_min = datetime.strptime(now.strftime("%Y/%m/%d"), "%Y/%m/%d")-timedelta(hours=4)
        fecha_max = fecha_min + timedelta(days=2)
        canales = Canal.objects.all();
        canales_json = list(Canal.objects.all().values());

        for canal in canales_json:
            cartelera = Programa.objects.filter(hora_inicio__range=(fecha_min, fecha_max),
                                                canal_emision_id=canal['id']).values().order_by('hora_inicio')

            canal['programacion'] = list(cartelera)
            print(list(cartelera))

        return render(request, 'tvguia_app/home.html', {'panel': canales_json, 'hora_actual': hora_actual})
    else:

        return render(request, 'tvguia_app/home.html')


@superuser_only
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
        the_canal = Canal.objects.get(nombre=programa['canal_emision'])
        cond1 = Programa.objects.filter(canal_emision=the_canal,
                                hora_inicio__gte=programa['hora_inicio'],
                                hora_inicio__lte=programa['hora_fin']).exists()
        cond2 = Programa.objects.filter(canal_emision=the_canal,
                                hora_fin__gte=programa['hora_inicio'],
                                hora_fin__lte=programa['hora_fin']).exists()
        cond3 = Programa.objects.filter(canal_emision=the_canal,
                                hora_inicio__lte=programa['hora_inicio'],
                                hora_fin__gte=programa['hora_fin']).exists()
        print("cond1",cond1)
        print("cond2", cond2)
        print("cond3", cond3)
        if not cond1 and not cond2 and not cond3:
            #print("no existe programa en esa hora")
            print("ERE")
            new_programa = Programa(
                hora_inicio=programa['hora_inicio'],
                hora_fin=programa['hora_fin'],
                titulo=programa['titulo'],
                imagen=programa['imagen'],
                tipo=programa['tipo'],
                duracion_total=programa['duracion_total'],
                canal_emision=the_canal,
            )
            programa_bulk.append(new_programa)

    Programa.objects.bulk_create(programa_bulk)
    return render(request, 'tvguia_app/home.html')


def about(request):
    """  MAIN PAGE """
    return render(request, 'tvguia_app/about.html')
