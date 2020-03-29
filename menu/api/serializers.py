from rest_framework import serializers
from menu.models import Ingredient, Menu


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name", "slug"]

        read_only_fields = ["slug"]


class MenuSerializer(serializers.ModelSerializer):

    # ingredients = IngredientSerializer(many=True, read_only=False)

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

        # extra_kwargs = {"ingredients": {"required": True}}
        read_only_fields = ["slug", "created_at"]
