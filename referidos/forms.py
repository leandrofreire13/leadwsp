from django import forms


from .models import Referido


class ReferidoForm(forms.ModelForm):
    class Meta:
        model = Referido
        fields = {'quem_indicou', 'nome', 'telefone', 'prioridade', 'status'}