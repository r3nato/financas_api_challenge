from finance_api.core.models import Category, Expense, Income
from rest_framework import serializers


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["category"] = instance.category.name
        return repr


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
