from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import ReferidoForm
from .models import Referido


# Create your views here.

def index(request):
    return render(request, 'referidos/inicio.html')

@login_required
def list_referidos(request):
    referidos = Referido.objects.all().order_by('-status')
    form = ReferidoForm(request.POST)
    return render(request, 'referidos/lista_referidos.html', {'referidos': referidos, 'form': form})


# Cria um novo referido
@login_required
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

@login_required
# Editar um referido
def referido_edit(request, pk):
    post = get_object_or_404(Referido, pk=pk)
    if request.method == "POST":
        form = ReferidoForm(request.POST, instance=post)
        if form.is_valid():
            referido = form.save(commit=False)
            referido.save()
            return redirect('referidos')
    else:
        form = ReferidoForm(instance=post)
    return render(request, 'referidos/referidos_form.html', {'form': form})