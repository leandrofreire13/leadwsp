from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import ReferidoForm
from .models import Referido


# Create your views here.

def index(request):
    return render(request, 'referidos/inicio.html')


def list_referidos(request):
    referidos = Referido.objects.filter()
    return render(request, 'referidos/lista_referidos.html', {'referidos': referidos})


# Cria um novo referido

def referido_new(request):
    if request.method == "POST":
        form = ReferidoForm(request.POST)
        if form.is_valid():
            referido = form.save(commit=False)
            referido.save()
            return redirect('referidos')
    else:
        form = ReferidoForm()
    return render(request, 'referidos/referidos_form.html', {'form': form})


# Editar um referido