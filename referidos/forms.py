from django import forms
from django.forms import TextInput

from .models import Referido


class ReferidoForm(forms.ModelForm):
    class Meta:
        model = Referido
        fields = ['aluno', 'aluno', 'nome', 'telefone', 'prioridade', 'status']
        widgets = {
            'aluno': TextInput(attrs={
                'class': "form-control"
            }),
            'nome': TextInput(attrs={
                'class': "form-control"
            }),
            'telefone': TextInput(attrs={
                'class': "form-control"
            }),

        }