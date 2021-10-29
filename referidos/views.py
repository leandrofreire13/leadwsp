from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Referido
from .forms import ReferidoForm


# Create your views here.

def index(request):
    return render(request, 'referidos/inicio.html')


def list_referidos(request):
    referidos = Referido.objects.filter()
    return render(request, 'referidos/lista_referidos.html', {'referidos': referidos})


# Cria um novo referido

def referido_new(request):
    return HttpResponse("Arrumar esse def para criar o forms")