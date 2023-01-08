from django.urls import include, path
from rest_framework import routers

from . import serializers, views

router = routers.DefaultRouter()
router.register("expenses", views.ExpenseViewSet, "expenses")
router.register("incomes", views.IncomeViewSet, "incomes")
router.register("categories", views.CategoryViewSet, "categories")

urlpatterns = [
    path("", include(router.urls), name="list"),
    path(
        "expenses/<int:year>/<int:month>/",
        views.MonthTransactions.as_view(
            type="expense", serializer_class=serializers.IncomeSerializer
        ),
        name="month-expenses",
    ),
    path(
        "incomes/<int:year>/<int:month>/",
        views.MonthTransactions.as_view(
            type="income", serializer_class=serializers.IncomeSerializer
        ),
        name="month-incomes",
    ),
    path(
        "summary/<int:year>/<int:month>/",
        views.MonthSummary.as_view(),
        name="month-summary",
    ),
]
