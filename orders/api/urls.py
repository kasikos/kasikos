from django.urls import path
from orders.api.views import checkout

app_name = "orders"

urlpatterns = [
    path('', checkout, name="checkout")
]
