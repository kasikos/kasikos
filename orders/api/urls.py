from django.urls import path
from orders.api.views import (
    orders
)

app_name = "orders"

urlpatterns = [
    path('', orders, name="checkout")
]
