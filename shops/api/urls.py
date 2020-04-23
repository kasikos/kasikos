from django.urls import path
from shops.api.views import (
    api_detail_shop_view,
    ShopView,
    ShopAPIView
)

app_name = "shops"
urlpatterns = [
    path("", ShopAPIView.as_view(), name="shop-create"),
    path("<slug>/", api_detail_shop_view, name="detail"),
]
