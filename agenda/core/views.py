from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

   #pega todos os eventos
   #evento = Evento.objects.all()

   #pega um evento
   #evento = Evento.objects.get(id=1)

   #cada usuário vê apenas o seus eventos
   evento = Evento.objects.filter(usuario=usuario)

   dados = dict({'eventos':evento})
   return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
   return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
   if request.POST:
      titulo = request.POST.get('titulo')
      data_evento = request.POST.get('data_evento')
      descricao = request.POST.get('descricao')
      usuario = request.user
      Evento.objects.create(titulo=titulo,
                            data_evento=data_evento,
                            descricao=descricao,
                            usuario=usuario)
   return redirect('/')