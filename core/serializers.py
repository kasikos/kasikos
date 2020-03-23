from .models import User
from .models import UserProfile
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["cellphone_no", "first_name", "last_name"]

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "cellphone_no", "profile_picture"]