from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.
#def index(request):
#  return redirect('/agenda/')

def lista_eventos(request):
   usuario = request.user

   #pega todos os eventos
   #evento = Evento.objects.all()
   #pega um evento
   #evento = Evento.objects.get(id=1)
   evento = Evento.objects.filter(usuario=usuario)

   dados = dict({'eventos':evento})
   return render(request, 'agenda.html', dados)