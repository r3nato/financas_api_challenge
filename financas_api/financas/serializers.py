from rest_framework import serializers
from rest_framework.validators import UniqueForMonthValidator
from  .models import Despesa, Receita, CategoriaDespesa


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = ['id', 'data', 'valor', 'descricao', 'categoria']
        validators = [
            UniqueForMonthValidator(
                queryset=Despesa.objects.all(),
                field='descricao',
                date_field='data',
                message='Um mesmo mês não pode ter duas despesas com mesma descrição.'
            )
        ]
    
    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['categoria'] = instance.get_categoria_display()
        return repr


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
        validators = [
            UniqueForMonthValidator(
                queryset=Receita.objects.all(),
                field='descricao',
                date_field='data',
                message='Um mesmo mês não pode ter duas receitas com mesma descrição.'
            )
        ]