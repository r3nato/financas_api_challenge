from django.db import models


class Income(models.Model):
    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()


class Expense(models.Model):

    class ExpenseCategory(models.TextChoices):
        FOOD = "FO", "Food"
        EDUCATION = "ED", "Education"
        PERSONAL = "PE", "Personal"
        HEALTH = "HE", "Health"
        HOUSING = "HO", "Housing"
        TRANSPORTATION = "TR", "Transportation"
        OTHER = "OT", "Other"

    description = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    category = models.CharField(
        max_length=2, 
        choices=ExpenseCategory.choices, 
        default=ExpenseCategory.OTHER
    )
