from rest_framework import serializers
from shops.models import Shop

class ShopSerializer(serializers.Serializer):
    class Meta:
        model = Shop
        fields = [
            'shop_name', 
            'slug',
            'user', 
            'street_name', 
            'town', 
            'zip_code', 
            'cellphone_no',
            'email',
            'tel_number',
            'description',
            'reg_no'
        ]