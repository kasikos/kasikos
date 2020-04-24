from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserProfileDetailView, UserProfileListCreateView

app_name = 'users'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),

    # Get all user profiles and create a new profile
    path('profiles/', UserProfileListCreateView.as_view(), name='profiles'),
    # Retrieve profile details of the currently logged in user
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile'),
]
