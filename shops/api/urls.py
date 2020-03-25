from django.urls import path
from shops.api.views import ShopView, ShopAPIView

app_name = 'shops'
urlpatterns = [
	path('', ShopAPIView.as_view(), name='shop-create'),
	path('<slug:slug>/', ShopView.as_view(), name='shops'),
]