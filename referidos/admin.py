from django.contrib import admin
from .models import Referido, Aluno


# Register your models here.
class CamposReferidos(admin.ModelAdmin):
    list_display = ('aluno','nome', 'telefone', 'prioridade', 'status')


admin.site.register(Referido, CamposReferidos)

# Register your models here.
class CamposAluno(admin.ModelAdmin):
    list_display = ('nome','matricula')


admin.site.register(Aluno, CamposAluno)
