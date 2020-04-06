from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from core.models import User
from core.models import UserProfile
from core.api.serializers import UserSerializer
from core.api.serializers import UserProfileSerializer

@api_view(['GET'])
def api_userprofile_view(request, slug):
    try:
        user_profile = UserProfile.objects.get(slug=slug)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

