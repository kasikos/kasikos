from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shops.api.serializers import ShopSerializer
from shops.models import Shop

class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shops to be viewed or edited
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = []