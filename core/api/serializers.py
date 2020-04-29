from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

from ..models import UserProfile

class UserSerializer:
    pass

class ProfileSerilizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
