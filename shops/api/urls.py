from django.urls import include, path
from rest_framework import routers
from shops.api import views

router = routers.DefaultRouter()
router.register(r'shops', views.ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
