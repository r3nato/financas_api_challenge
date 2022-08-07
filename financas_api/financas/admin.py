from django.contrib import admin
from .models import Despesa, Receita

class DespesaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'valor', 'descricao')
    class Meta:
        model = Despesa

admin.site.register(Despesa, DespesaAdmin)


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'valor', 'descricao')
    class Meta:
        model = Receita

admin.site.register(Receita, ReceitaAdmin)
