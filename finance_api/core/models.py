from django.db import models


class Income(models.Model):
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return self.description


class Expense(models.Model):
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
