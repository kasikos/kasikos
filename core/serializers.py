from .models import User
from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "profile_picture"]
