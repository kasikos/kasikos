from rest_framework import serializers
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

from ..models import UserProfile
from shops.models import Shop


class UserSerializer(serializers.ModelSerializer):
    shops = serializers.PrimaryKeyRelatedField(many=True, queryset=Shop.objects.all())
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerilizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
