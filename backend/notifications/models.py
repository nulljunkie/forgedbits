from typing import override

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    @override
    def __str__(self):
        return self.name


class Order(models.Model):
    quantity = models.IntegerField()
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total(self):
        return self.quantity * self.price_per_item * .9
