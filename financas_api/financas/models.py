from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()


class Despesa(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data = models.DateField()
