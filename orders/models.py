from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.conf import settings

from menu.models import Ingredient, Menu
from shops.models import Shop


USER = settings.AUTH_USER_MODEL

class OrderItem(models.Model):
    title = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customer = models.ForeignKey(USER, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Order(models.Model):
    customer = models.ForeignKey(USER, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    order_no = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self):
        return self.customer.get_full_name()
