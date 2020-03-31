from django.urls import path
from core.api.views import UserView, UserAPIView
from core.api.views import UserProfileView, UserProfileAPIView

app_name = 'core'
urlpatterns = [
	path('', UserAPIView.as_view(), name='user-create'),
	path('<slug:slug>/', UserView.as_view(), name='users'),

    path('', UserProfileAPIView.as_view(), name='userprofile-create'),
    path('<slug:slug>/', UserProfileView.as_view(), name='userprofiles'),
]