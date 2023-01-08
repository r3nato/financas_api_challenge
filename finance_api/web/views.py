from django.db.models import F, Sum
from finance_api.core.models import Category, Expense, Income
from rest_framework import filters, generics, response, views, viewsets

from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["description"]


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["description"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]


class MonthTransactions(generics.ListAPIView):
    type: str = ""

    def get_queryset(self):
        if self.type == "expense":
            return Expense.objects.filter(
                data__year=self.kwargs["year"], data__month=self.kwargs["month"]
            )
        else:
            return Income.objects.filter(
                data__year=self.kwargs["year"], data__month=self.kwargs["month"]
            )


class MonthSummary(views.APIView):
    def get(self, request, year, month):
        date_filter = {"date__month": month, "date__year": year}
        month_incomes = Income.objects.filter(**date_filter).aggregate(
            Sum("value", default=0)
        )["value__sum"]
        month_expenses = Expense.objects.filter(**date_filter).aggregate(
            Sum("value", default=0)
        )["value__sum"]
        expense_per_category = (
            Expense.objects.filter(**date_filter)
            .values("category__name")
            .annotate(category_expense=Sum("value", default=0))
        )
        month_total = month_incomes - month_expenses

        return response.Response(
            {
                "incomes": month_incomes,
                "expenses": month_expenses,
                "expense_per_category": expense_per_category,
                "total": month_total,
            }
        )
