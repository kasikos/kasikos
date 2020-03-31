from django.db.models import Q
from rest_framework import generics, mixins

from core.models import User
from core.models import UserProfile
from core.api.permissions import IsOwnerOrReadOnly
from core.api.serializers import UserSerializer
from core.api.serializers import UserProfileSerializer


class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows users to be listed, Created and Searched   
    """
    lookup_field 		= 'slug'
    serializer_class	= UserSerializer

    def get_queryset(self):
    	qs = User.objects.all()
    	query = self.request.GET.get("q")
    	if query is not None:
    		qs = qs.filter(
    				Q(cellphone_no__icontains=query)|
    				Q(first_name__icontains=query)
    				).distinct()
    	return qs

    def perform_create(self, serializer):
    	serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
    	return self.create(request, *args, **kwargs)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows user to be viewed, edited or deleted via user slug
    """
    lookup_field 		= 'slug'
    serializer_class	= UserSerializer
    permission_classes	= [IsOwnerOrReadOnly]

    def get_queryset(self):
    	return User.objects.all()

class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows user profile to be listed, Created and Searched   
    """
    lookup_field 		= 'slug'
    serializer_class	= UserProfileSerializer

    def get_queryset(self):
    	qs = UserProfile.objects.all()
    	query = self.request.GET.get("q")
    	if query is not None:
    		qs = qs.filter(Q(email__icontains=query)).distinct()
    	return qs

    def perform_create(self, serializer):
    	serializer.save(userProfile=self.request.userProfile)

    def post(self, request, *args, **kwargs):
    	return self.create(request, *args, **kwargs)


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows user to be viewed, edited or deleted via user slug
    """
    lookup_field 		= 'slug'
    serializer_class	= UserProfileSerializer
    permission_classes	= [IsOwnerOrReadOnly]

    def get_queryset(self):
    	return UserProfile.objects.all()
