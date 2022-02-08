from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)

    #aceita descricao em branco ou nula
    descricao = models.TextField(blank=True, null=True)

    #verbose_name altera o título para 'Data do Evento'
    data_evento = models.DateTimeField(verbose_name='Data do Evento')

    #captura a data que o usuário inseriu o evento no bacno
    #auto_now insere automaticamente a hora atual, independente do usuário
    data_criacao = models.DateTimeField(auto_now=True)

    #para criar multiplos usuarios
    #models.CASCADE --> se for excluido o usuario, exclui também os eventos dele
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #tabela
    class Meta:
        db_table = 'evento'

    def __str__(self):
        #sempre que chamar o título, retorna
        return self.titulo
