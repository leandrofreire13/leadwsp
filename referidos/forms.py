from django import forms


from .models import Referido


class ReferidoForm(forms.ModelForm):
    class Meta:
        model = Referido
        fields = {'nome', 'telefone', 'prioridade', 'status'}