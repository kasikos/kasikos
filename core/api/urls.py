from django.urls import path
from core.api.views import api_userprofile_view

app_name = 'core'
urlpatterns = [
	path('<slug>/', api_userprofile_view, name="userprofile")
]