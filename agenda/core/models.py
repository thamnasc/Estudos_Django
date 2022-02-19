from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Evento(models.Model):
    titulo = models.CharField(max_length=100)

    #aceita descricao em branco ou nula
    descricao = models.TextField(blank=True, null=True)

    #verbose_name altera o título para 'Data do Evento'
    data_evento = models.DateTimeField(verbose_name='Data do Evento')

    #captura a data que o usuário inseriu o evento no bacno
    #auto_now insere automaticamente a hora atual, independente do usuário
    data_criacao = models.DateTimeField(auto_now=True)

    #para escrever o local ou onde vai acontecer o evento
    local_evento = models.TextField(default='', blank=True, null=True)

    #para criar multiplos usuarios
    #models.CASCADE --> se for excluido o usuario, exclui também os eventos dele
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #a  tabela é chamada por 'evento'
    class Meta:
        db_table = 'evento'

    def __str__(self):
        #sempre que chamar o título, retorna e mostra o nome do título
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %Hh%M')

    def get_local_evento(self):
        return self.local_evento

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False