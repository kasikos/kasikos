from rest_framework import serializers

from orders.models import OrderItem, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'customer',
            'items',
            'ordered',
            'start_date',
            'ordered_date',
            'order_no'
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'title',
            'menu',
            'customer',
            'ingredients',
            'ordered',
            'quantity'
        ]
