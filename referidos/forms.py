from django import forms
from django.forms import TextInput

from .models import Referido


class ReferidoForm(forms.ModelForm):
    class Meta:
        model = Referido
        fields = ['nome', 'telefone', 'prioridade', 'status']
       