from rest_framework import viewsets, filters, generics, views, response
from .models import Despesa, CategoriaDespesa, Receita
from .serializers import DespesaSerializer, ReceitaSerializer
from django.db.models import Sum, When, Value, Case, CharField

class DespesaViewset(viewsets.ModelViewSet):
    """Exibindo as despesas cadastradas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["descricao"]


class ReceitaViewset(viewsets.ModelViewSet):
    """Exibindo as receitas cadastradas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["descricao"]


class TransacoesMes(generics.ListAPIView):
    tipo: str = ''

    def get_queryset(self):
        if self.tipo == 'despesa':
            return Despesa.objects.filter(
                    data__year=self.kwargs['ano'], 
                    data__month=self.kwargs['mes']
            )
        else:
            return Receita.objects.filter(
                    data__year=self.kwargs['ano'], 
                    data__month=self.kwargs['mes']
            )


class ResumoMes(views.APIView):

    def get(self, request, ano, mes):
        filtro_mes_ano = {'data__month':mes, 'data__year':ano}
        receitas_mes = Receita.objects.filter(**filtro_mes_ano).aggregate(Sum('valor'))['valor__sum'] or 0
        despesas_mes = Despesa.objects.filter(**filtro_mes_ano).aggregate(Sum('valor'))['valor__sum'] or 0
        whens_categorias = [When(categoria=k, then=Value(v)) for k, v in CategoriaDespesa.choices]
        despesas_categorias_mes = Despesa.objects.filter(**filtro_mes_ano).annotate(nome_categoria=Case(*whens_categorias, output_field=CharField())).values("nome_categoria").annotate(
            despesa_categoria=Sum("valor"))
        total_mes = receitas_mes - despesas_mes

        return response.Response({
            "receitas": receitas_mes, 
            "despesas": despesas_mes,
            "despesas_por_categoria": despesas_categorias_mes,
            "total": total_mes
        })
