from rest_framework import viewsets, filters, generics, views
from .models import Despesa, Receita
from .serializers import DespesaSerializer, ReceitaSerializer


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
