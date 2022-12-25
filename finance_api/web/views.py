from rest_framework import viewsets, filters, generics, views, response
from finance_api.core.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from django.db.models import Sum, When, Value, Case, CharField

class ExpenseViewset(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["description"]


class IncomeViewset(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["description"]


class MonthTransactions(generics.ListAPIView):
    type: str = ''

    def get_queryset(self):
        if self.tipo == 'expense':
            return Expense.objects.filter(
                    data__year=self.kwargs['ano'], 
                    data__month=self.kwargs['mes']
            )
        else:
            return Income.objects.filter(
                    data__year=self.kwargs['ano'], 
                    data__month=self.kwargs['mes']
            )


class MonthSummary(views.APIView):

    def get(self, request, year, month):
        date_filter = {'date__month': month, 'date__year': year}
        month_incomes = Income.objects.filter(**date_filter).aggregate(Sum('value'))['value__sum'] or 0
        month_expenses = Expense.objects.filter(**date_filter).aggregate(Sum('value'))['value__sum'] or 0
        whens_categories = [When(category=k, then=Value(v)) for k, v in Expense.ExpenseCategory.choices]
        despesas_categorias_mes = Expense.objects.filter(**date_filter).annotate(category_name=Case(*whens_categories, output_field=CharField())).values("category_name").annotate(
            category_expense=Sum("valor"))
        month_total = month_incomes - month_expenses

        return response.Response({
            "incomes": month_incomes, 
            "expenses": month_expenses,
            "expense_per_category": despesas_categorias_mes,
            "total": month_total
        })
