from django.shortcuts import render
from django.http import HttpResponse

from .models import Referido


# Create your views here.

def index(request):
    return render(request, 'referidos/inicio.html')


def list_referidos(request):
    referidos = Referido.objects.filter()
    return render(request, 'referidos/lista_referidos.html', {'referidos': referidos})