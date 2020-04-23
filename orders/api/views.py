from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.conf import settings

from orders.models import OrderItem, Order
from orders.api.serializers import (
    OrderSerializer,
    OrderItemSerializer
)

USER = settings.AUTH_USER_MODEL


@api_view(['GET', ])
def orders(request):
    try:
        orders = Order.objects.all()
    except Exception as e:
        raise e

@api_view(['POST'])
def a():
    pass
