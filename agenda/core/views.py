from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

#def index(request):
#  return redirect('/agenda/')

def login_user(request):
   # página para fazer autenticação de usuário
   return render(request, 'login.html')

def submit_login(request):
   if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')
      usuario = authenticate(username=username, password=password)
      if usuario is not None:
         login(request, usuario)
         return redirect('/')
      else: #se errar o login
         messages.error(request, "Usuário ou senha inválidos")
   #se não for um POST ou se não estiver autenticado
   return redirect('/')

def logout_user(request):
   logout(request)
   return redirect('/')

# não abre views quando estiver autenticado
# é redirecionado ao login
@login_required(login_url='/login/')
def lista_eventos(request):

   usuario = request.user

   data_atual = datetime.now() - timedelta(hours=1)

   #pega todos os eventos
   #evento = Evento.objects.all()

   #pega um evento
   #evento = Evento.objects.get(id=1)

   #cada usuário vê apenas o seus eventos
   evento = Evento.objects.filter(usuario=usuario,
                                  #mostra os eventos futuros
                                  data_evento__gt=data_atual)

   dados = dict({'eventos':evento})
   return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):

   id_evento = request.GET.get('id')
   dados = {}
   if id_evento:
      dados['evento'] = Evento.objects.get(id=id_evento)
   return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):

   if request.POST:
      titulo = request.POST.get('titulo')
      data_evento = request.POST.get('data_evento')
      descricao = request.POST.get('descricao')
      local_evento = request.POST.get('local_evento')
      usuario = request.user
      id_evento= request.POST.get('id_evento')
      if id_evento:
         evento = Evento.objects.get(id=id_evento)
         if evento.usuario == usuario:
            evento.titulo = titulo
            evento.descricao = descricao
            evento.data_evento = data_evento
            evento.save()

         # mesmo que o if a cima
         #Evento.objects.filter(id=id_evento).update(titulo=titulo,
         #                                           data_evento=data_evento,
         #                                            descricao=descricao)
      else:
         Evento.objects.create(titulo=titulo,
                               data_evento=data_evento,
                               descricao=descricao,
                               local_evento=local_evento,
                               usuario=usuario)
   return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):

   usuario = request.user
   try:
      evento = Evento.objects.get(id=id_evento)
   except Exception: # se evento não existe
      raise Http404()
   if usuario == evento.usuario:
      evento.delete()
   else: # se outro usuário, que não for dono do evento, tentar excluir
      raise Http404()
   return redirect('/')

# para pegar informações da agenda por uma API ou aplicação externa, por exemplo, sem precisar de usar o usuário
# @login_required(login_url='/login/')
def json_lista_evento(request, id_usuario):

   # cria Json para cada usuário
   usuario = User.objects.get(id=id_usuario)

   #cada usuário vê apenas o seus eventos
   evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')

   # safe é preciso porque é passada uma lista, não um dicionário
   return JsonResponse(list(evento), safe=False)