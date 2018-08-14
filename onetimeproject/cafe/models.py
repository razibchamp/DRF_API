from django.db import models

# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name

class Order(models.Model):
    meals = models.ManyToManyField(Meal)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name