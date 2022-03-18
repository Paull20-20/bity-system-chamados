from dataclasses import field
from django import forms

from .models import Chamado_geral

class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado_geral
        fields = ('titulo', 'descrição')


class ChamadoForm2(forms.ModelForm):
    class Meta:
        model = Chamado_geral
        fields = ('titulo', 'descrição', 'arquivo', 'Status')
    #Arquivo = forms.FileField(
     #   label='Selecione um anexo',
     #   help_text='max. 42 megabytes'
    #)




