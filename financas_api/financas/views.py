from rest_framework import viewsets
from .models import Despesa, Receita
from .serializers import DespesaSerializer, ReceitaSerializer

class DespesaViewset(viewsets.ModelViewSet):
    """Exibindo as despesas cadastradas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer


class ReceitaViewset(viewsets.ModelViewSet):
    """Exibindo as receitas cadastradas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer