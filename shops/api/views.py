from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from shops.models import Shop
from shops.api.permissions import IsOwnerOrReadOnly
from shops.api.serializers import ShopSerializer


@api_view(['GET', ])
def api_detail_shop_view(request, slug):
    try:
        shop = Shop.objects.get(slug=slug)
    except Shop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

class ShopAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows shops to be listed, Created and Serched
    """

    lookup_field = "slug"
    serializer_class = ShopSerializer

    def get_queryset(self):
        qs = Shop.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(shop_name__icontains=query) | Q(street_name__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShopView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows shop to be viewed or edited or deleted via its slug
    """

    lookup_field = "slug"
    serializer_class = ShopSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Shop.objects.all()
