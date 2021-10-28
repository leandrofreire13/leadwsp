from django.contrib import admin
from .models import Referido


# Register your models here.
class CamposReferidos(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'prioridade', 'status')


admin.site.register(Referido, CamposReferidos)
