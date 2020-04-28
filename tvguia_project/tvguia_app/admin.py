from django.contrib import admin

# Register your model here.
from .model.canal import Canal
from .model.deporte import Deporte
from .model.documental import Documental
from .model.serie import Serie, Episodio
from .model.otro import Otro
from .model.pelicula import Pelicula
from .model.noticias import Noticias
from .model.programa import Programa

admin.site.register(Canal)
admin.site.register(Programa)

'''
admin.site.register(Deporte)
admin.site.register(Documental)
admin.site.register([Serie, Episodio])
admin.site.register(Otro)
admin.site.register(Pelicula)
admin.site.register(Noticias)
'''
