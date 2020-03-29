from rest_framework import serializers
from shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    # uri         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Shop
        fields = [
            # 'uri',
            "shop_name",
            "slug",
            "user",
            "street_name",
            "town",
            "zip_code",
            "cellphone_no",
            "email",
            "tel_number",
            "description",
            "reg_no",
            "logo",
            "created_at",
            "updated_at",
        ]

    # def validate_shop_name(self, value):
