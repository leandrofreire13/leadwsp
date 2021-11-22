from django import forms
from django.forms import TextInput

from .models import Referido


class ReferidoForm(forms.ModelForm):
    class Meta:
        model = Referido
        fields = ['quem_indicou', 'nome', 'telefone', 'prioridade', 'status']
        widgets = {
            'quem_indicou': TextInput(attrs={
                'class': "form-control"
            }),
            'nome': TextInput(attrs={
                'class': "form-control"
            }),
            'telefone': TextInput(attrs={
                'class': "form-control"
            }),

        }