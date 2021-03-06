from django.db import models

"""
    Modelo de referido com os seguintes campos.
        Nome de quem indicou (Criar como um model)
        Nome do referido
        Telefone
        Proridade
        Status 
        Whatsapp ** Não precisa eu acho
        Data
        Hora
"""

STATUS_REFERIDOS = (
    ('Iniciar', 'INICIAR'),
    ('Ligação 1', 'LIGACAO_1'),
    ('Ligação 2', 'LIGACAO_2'),
    ('Ligação 3', 'LIGACAO_3'),
    ('Mandar áudio','MANDA_AUDIO'),
    ('Áudio enviado','AUDIO_ENVIADO'),
    ('Agendado','AGENDADO'),
    ('Mandar texto','MANDAR_TEXTO'),
    ('Texto enviado','TEXTO_ENVIADO'),
    ('Não venda','NAO_VENDA'),
    ('Venda','VENDA'),
)

MATRICULA = (
   ('Aluno', 'Aluno'),
   ('Não Aluno', 'Não Aluno')
)
 
PRIORIDADE = (
   ('Neutro', 'Neutro'),
   ('Sim', 'Sim'),
   ('Não', 'Não')
)

class Aluno(models.Model):
   nome = models.CharField(max_length=200)
   matricula = models.CharField(max_length=200, choices=MATRICULA, default='Aluno')

   def __str__(self):
       return self.nome


class Referido(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=200, choices=PRIORIDADE, default="Neutro")
    status = models.CharField(max_length=200, choices=STATUS_REFERIDOS, default='Iniciar')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

