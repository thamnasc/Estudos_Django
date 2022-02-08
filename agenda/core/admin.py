from django.contrib import admin
from core.models import Evento

# Register your models here.

#registro do model

class EventoAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)