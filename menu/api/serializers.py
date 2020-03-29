from rest_framework import serializers
from menu.models import Ingredient, Menu


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name", "slug"]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "title",
            "slug",
            "shop",
            "ingredients",
            "price",
            "description",
            "image",
            "created_at",
            "updated_at",
        ]
