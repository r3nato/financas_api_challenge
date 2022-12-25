from finance_api.core.models import Expense, Income
from rest_framework import serializers
from rest_framework.validators import UniqueForMonthValidator


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "date", "value", "description", "category"]

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["category"] = instance.get_category_display()
        return repr


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"
