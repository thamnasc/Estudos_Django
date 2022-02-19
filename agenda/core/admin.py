from django.contrib import admin
from core.models import Evento

# registro do model

class EventoAdmin (admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao', 'local_evento')
    list_filter = ('titulo', 'usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)