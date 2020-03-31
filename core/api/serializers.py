from rest_framework import serializers
from core.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'active', 
            'first_name', 
            'last_name', 
            'cellphone_no', 
            'is_shopowner', 
            'is_staff', 
            'is_superuser'
        ]