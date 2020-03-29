from django.db.models import Q
from rest_framework import generics, mixins

from menu.models import Ingredient, Menu
from shops.models import Shop
from menu.api.serializers import IngredientSerializer, MenuSerializer
from shops.api.serializers import ShopSerializer


class MenuAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows menu to be listed, Created and Serched   
    """

    lookup_field = "slug"
    serializer_class = MenuSerializer

    def get_queryset(self):
        qs = Menu.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) | Q(ingredients__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(shop=self.request.shop)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MenuView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows menu to be viewed or edited or deleted via its slug
    """

    lookup_field = "slug"
    serializer_class = MenuSerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Menu.objects.all()


class IngredientsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "slug"
    serializer_class = IngredientSerializer

    def get_queryset(self):
        qs = Ingredient.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(name_icontains=query)
            ).distinct()
        return qs

    # def perform_create(self, serializer):
    #     serializer.save(name=self.request.name)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        


class IngredientView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "slug"
    serializer_class = IngredientSerializer

    def get_queryset(self):
        return Ingredient.objects.all()