#-*- coding: utf-8 -*-


from django.db import models
import datetime
from ..model.canal import Canal

TIPO_CHOICES = (
    ('otros', '0'),
    ('pelicula', '1'),
    ('serie', '2'),
    ('noticia', '3'),
    ('documental', '4'),
    ('deporte', '5'),
    ('infantil', '6'),

)





class Programa(models.Model):
    class Meta:
        ordering = ['hora_inicio']

    hora_inicio = models.DateTimeField(blank=True)
    hora_fin = models.DateTimeField(blank=True)
    duracion_total = models.IntegerField(default=0)


    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000, null=True)
    edad = models.IntegerField(default=0)
    puntuacion = models.IntegerField(null=True,blank=True)
    imagen = models.CharField(max_length=500, null=True)
    temporada = models.CharField(max_length=500, default="NONE", null=True)

    tipo = models.CharField(choices=TIPO_CHOICES, default='otros', max_length=100)


    canal_emision = models.ForeignKey(Canal, related_name='canal_programa', on_delete=models.CASCADE)

    def __str__(self):
        return "{}--{}--{}".format(self.canal_emision, (self.hora_inicio).strftime("%d %H:%M"),self.titulo)

    @classmethod
    def getDuracion(self,hora_fin , hora_inicio):
        # inicio = datetime.strptime((self.hora_inicio,"%H:i"))
        # fin =  datetime.strptime((self.hora_fin,"%H:i"))
        duracion = hora_fin - hora_inicio

        minutes = divmod(duracion.seconds, 60)
        print('Difference in minutes: ', minutes[0], 'minutes',
              minutes[1], 'seconds')
        return int(minutes[0])


    def save(self, *args, **kwargs):

        self.duracion_total = self.getDuracion(self.hora_fin , self.hora_inicio)
        super(Programa, self).save(*args, **kwargs)


