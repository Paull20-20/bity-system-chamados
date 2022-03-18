from django.db import models
from django.contrib.auth import get_user_model
#from turtle import title
#import matplotlib matplotlib.use('Agg')  # Must be done before importing pyplot import matplotlib.pyplot as plt

#import tkinter
#top = tkinter.Tk();
#top = tkinter.mainloop();

# Create your models here. esse

class Chamado_geral(models.Model):

    STATUS = (
        ('Solicitado', 'Solicitado'),       # Solicitado
        ('Em_andamento', 'Em_andamento'),   # em andamento
        ('Concluído', 'Concluído'),         # concluido
      
    )

    titulo = models.CharField("Título:", max_length=255)
    descrição = models.TextField("Descrição:")
    arquivo = models.FileField("Anexo:", upload_to='',  blank=True, null=True)
    Status = models.CharField(
        max_length=20,
        choices=STATUS,
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    #com esse comando abaixo pegamos a data da solicitação
    created_at = models.DateTimeField(auto_now_add=True)
    # o comando abaixo serve para sempre que alguém alterar o status o db seja atualizado de acordo
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titulo #com isso no painel terá o título em cada chamado.



        #testes testes



