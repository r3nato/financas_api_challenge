from django.db import models


class CategoriaDespesa(models.TextChoices):
    ALIMENTACAO = "A", "Alimentação"
    IMPREVISTOS = "I", "Imprevistos"
    EDUCACAO = "E", "Educação"
    LAZER = "L", "Lazer"
    SAUDE = "S", "Saúde"
    MORADIA = "M", "Moradia"
    TRANSPORTE = "T", "Transporte"
    OUTRAS = "O", "Outras"

class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(
        max_length=1, 
        choices=CategoriaDespesa.choices, 
        default=CategoriaDespesa.OUTRAS
    )
