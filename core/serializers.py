from .models import User
from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile 
        fields = ["id", "cellno", "profile_picture"]

class ShopsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shops
        fields = ["user", "shop_name", "street_name", "town", "zip_code", "tel_no", "email", "whatsapp_no"]

user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=50)
    street_name = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    tel_no = models.CharField(max_length=15)
    email = models.CharField(max_length=200, null=True)