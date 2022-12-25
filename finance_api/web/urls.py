from django.urls import path, include
from . import views, serializers
from rest_framework import routers

router = routers.DefaultRouter()
router.register('expenses', views.ExpenseViewset, 'expenses')
router.register('incomes', views.IncomeViewset, 'incomes')

urlpatterns = [
    path('', include(router.urls), name='list'),
    path(
        'expenses/<int:year>/<int:month>/', 
        views.MonthTransactions.as_view(
            type='expense',
            serializer_class=serializers.IncomeSerializer
        ),
        name="month-expenses"
    ),
    path(
        'incomes/<int:year>/<int:month>/', 
        views.MonthTransactions.as_view(
            type='income',
            serializer_class=serializers.IncomeSerializer
        ),
        name="month-incomes"
    ),
    path(
        'summary/<int:year>/<int:month>/',
        views.MonthSummary.as_view(),
        name="month-summary"
    )
]